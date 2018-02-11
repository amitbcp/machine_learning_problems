"--- encoding utf-8 ---"
''' Basic Word to Vector Model Implementation'''

import argparse
import collections
import math
import os
import random
import sys
import urllib
import zipfile
from tempfile import gettempdir

import numpy as np
import tensorflow as tf
from tensorflow.contrib.tensorboard.plugins import projector

# Give a folder path as an argument with '--log_dir' to save
# TensorBoard summaries. Default is a log folder in current directory.
current_path = os.path.dirname(os.path.realpath(sys.argv[0]))

parser = argparse.ArgumentParser()
parser.add_argument(
    '--log_dir',
    type=str,
    default=os.path.join(current_path, 'log'),
    help='The log directory for TensorBoard summaries.')
FLAGS, unparsed = parser.parse_known_args()

# Create the directory for TensorBoard variables if there is not.
if not os.path.exists(FLAGS.log_dir):
    os.makedirs(FLAGS.log_dir)

### Step 1 : Download Data

url = 'http://mattmahoney.net/dc/'
vocabulary = None
vocabulary_size = 50000
data_index = 0
num_steps = 10


def maybe_download(filename, expected_bytes):
    """Download a file if not present, & make sure its' the right size"""
    local_filename = os.path.join(gettempdir(), filename)
    if not os.path.exists(local_filename):
        local_filename, _ = urllib.request.urlretrieve(url + filename, local_filename)

    statinfo = os.stat(local_filename)
    if statinfo.st_size == expected_bytes:
        print("Found & verified download : {} ".format(filename))
    else:
        print(statinfo.st_size)
        # raise Exception('Failed to verify : {} \nDownload it again'.format(local_filename))
        local_filename = os.path.join(os.path.dirname(__file__), 'data/' + filename)
    # print(local_filename)
    return local_filename


# Read the data in to a list of strings after uzipping the file
def read_data(filename):
    """Extract the first file enclosed in a zip files as a list of words"""
    with zipfile.ZipFile(filename) as f:
        data = tf.compat.as_str(f.read(f.namelist()[0])).split()
    return data


### Step 2 : Build the dictionary and replace rare words with UNK Tokens

def build_dataset(words, n_words):
    """

    Process raw data into datasets.

    Arguments :
    words-- All the words read for the data file
    n_words-- Top n words that we want to have in our Vocabulary

    Returns :
    data-- List of index for all the words (integers from 0 to vocabulary_size-1) .This is the original text but words are replaced by their codes
    count-- map of words(strings) to count of occurrences
    dictionary-- Dictionary of word & it's index || map of words(strings) to their codes(integers)
    reversed_dictionary-- Reversed Dictionary || maps codes(integers) to words(strings)

    """

    count = [['UNK', -1]]
    count.extend(collections.Counter(words).most_common(n_words - 1))
    # print("Waiting for Debugger View of count")
    dictionary = dict()  # The dictionary gets loaded with the top words only and their index others get a value )
    for word, _ in count:
        dictionary[word] = len(dictionary)
    data = list()
    unk_count = 0
    for word in words:
        index = dictionary.get(word, 0)
        # All words other than Top n_words get ) and become UNK count
        if index == 0:  # dictionary['UNK']
            unk_count += 1
        data.append(index)
    count[0][1] = unk_count  # updating the count of UNK
    reversed_dictionary = dict(zip(dictionary.values(), dictionary.keys()))

    return data, count, dictionary, reversed_dictionary


# Step 3 : Function to generate a training batch for the skip-gram model
def generate_batch(data, batch_size=8, num_skips=2, skip_window=1):
    global data_index
    assert batch_size % num_skips == 0
    assert num_skips <= 2 * skip_window

    batch = np.ndarray(shape=(batch_size), dtype=np.int32)
    labels = np.ndarray(shape=(batch_size, 1), dtype=np.int32)
    span = 2 * skip_window + 1  # [skip window target skip window]
    buffer = collections.deque(maxlen=span)
    if data_index + span > len(data):
        data_index = 0
    buffer.extend(data[data_index:data_index + span])
    data_index += span

    for i in range(batch_size // num_skips):
        context_words = [w for w in range(span) if w != skip_window]  # excluding the target word
        words_to_use = random.sample(context_words, num_skips)
        for j, context_words in enumerate(words_to_use):
            batch[i * num_skips + j] = buffer[skip_window]
            labels[i * num_skips + j, 0] = buffer[context_words]
        if data_index == len(data):
            buffer.extend(data[0:span])
            data_index = span
        else:
            buffer.append(data[data_index])
            data_index += 1
        # Backtrack a little bit to avoid skipping wprds in the end of a batch
    data_index = (data_index + len(data) - span) % len(data)
    return batch, labels


filename = maybe_download('text8.zip', 3144016)
vocabulary = read_data(filename)
data, count, dictionary, reverse_dictionary = build_dataset(vocabulary, vocabulary_size)


# Step 4 : Build a Tensor Flow Graph for skipgram model

def build_graph(batch_size=128, embedding_size=128, skip_window=1, num_skips=2, num_sampled=64, valid_size=16,
                valid_window=100, ):
    """
     We pick a random validation set to sample nearest neighbors. Here we limit the
    validation samples to the words that have a low numeric ID, which by
    construction are also the most frequent. These 3 variables are used only for
    displaying model accuracy, they don't affect calculation.

    Arguments :
    :param batch_size:
    :param embedding_size: Dimension of the embedding vector.
    :param skip_window: How many words to consider left and right.
    :param num_skips: How many times to reuse an input to generate a label.
    :param num_sampled: Number of negative examples to sample.
    :param valid_size: Random set of words to evaluate similarity on.
    :param valid_window: Only pick dev samples in the head of the distribution.

    :return: TensorFlow final embeddings

    """
    graph = tf.Graph()
    with graph.as_default():
        # Input Data
        with tf.name_scope('inputs'):
            valid_examples = np.random.choice(valid_window, valid_size, replace=False)
            train_inputs = tf.placeholder(tf.int32, shape=[batch_size])
            train_labels = tf.placeholder(tf.int32, shape=[batch_size, 1])
            valid_dataset = tf.constant(valid_examples, dtype=tf.int32)

        # Look up embeddings for inputs.
        with tf.name_scope('embeddings'):
            embeddings = tf.Variable(tf.random_uniform([vocabulary_size, embedding_size], -1.0, 1.0))
            embed = tf.nn.embedding_lookup(embeddings, train_inputs)

        # Variables for NCE Loss
        with tf.name_scope('weights'):
            nce_weights = tf.Variable(
                tf.truncated_normal([vocabulary_size, embedding_size], stddev=1.0 / math.sqrt(embedding_size)))
        with tf.name_scope('biases'):
            nce_biases = tf.Variable(tf.zeros([vocabulary_size]))

            # Compute the average NCE loss for the batch.
            # tf.nce_loss automatically draws a new sample of the negative labels each
            # time we evaluate the loss.
            # Explanation of the meaning of NCE loss:
            #   http://mccormickml.com/2016/04/19/word2vec-tutorial-the-skip-gram-model/

        with tf.name_scope('loss'):
            loss = tf.reduce_mean(
                tf.nn.nce_loss(weights=nce_weights,
                               biases=nce_biases,
                               labels=train_labels,
                               inputs=embed,
                               num_sampled=num_sampled,
                               num_classes=vocabulary_size))

        # Adding the list value as a scalar to summary
        tf.summary.scalar('loss', loss)

        # Constructing a SGD optimizer using a learning rate of 1.0
        with tf.name_scope('optimizer'):
            optimizer = tf.train.GradientDescentOptimizer(1.0).minimize(loss)

        # Compute teh cosine similarty between minibatch examples & all embeddings
        norm = tf.sqrt(tf.reduce_sum(tf.square(embeddings), 1, keep_dims=True))
        normalized_embeddings = embeddings / norm
        valid_embeddings = tf.nn.embedding_lookup(normalized_embeddings, valid_dataset)

        similarity = tf.matmul(valid_embeddings, normalized_embeddings, transpose_b=True)

        # Merge all summaries.
        merged = tf.summary.merge_all()

        # Add a variable initializer
        init = tf.global_variables_initializer()

        # Create a saver
        saver = tf.train.Saver()

        # Step 5 : Begin Training
        with tf.Session(graph=graph) as session:
            # Opening a Writer to write summaries.
            writer = tf.summary.FileWriter(FLAGS.log_dir, session.graph)

            # Initializing Variables
            init.run()
            print('Initialized')
            average_loss = 0
            for step in range(num_steps):
                batch_inputs, batch_labels = generate_batch(data, batch_size, num_skips,
                                                            skip_window)
                feed_dict = {train_inputs: batch_inputs, train_labels: batch_labels}

                # Define metadata variable.
                run_metadata = tf.RunMetadata()

                # We perform one update step by evaluating the optimizer op (including it
                # in the list of returned values for session.run()
                # Also, evaluate the merged op to get all summaries from the returned "summary" variable.
                # Feed metadata variable to session for visualizing the graph in TensorBoard.
                _, summary, loss_val = session.run(
                    [optimizer, merged, loss],
                    feed_dict=feed_dict,
                    run_metadata=run_metadata)
                average_loss += loss_val

                # Add returned summaries to writer in each step.
                writer.add_summary(summary, step)
                # Add metadata to visualize the graph for the last run.
                if step == (num_steps - 1):
                    writer.add_run_metadata(run_metadata, 'step%d' % step)

                if step % 2000 == 0:
                    if step > 0:
                        average_loss /= 2000
                    # The average loss is an estimate of the loss over the last 2000 batches.
                    print('Average loss at step ', step, ': ', average_loss)
                    average_loss = 0

                # Note that this is expensive (~20% slowdown if computed every 500 steps)
                if step % 25000 == 0:
                    sim = similarity.eval()
                    for i in range(valid_size):
                        valid_word = reverse_dictionary[valid_examples[i]]
                        top_k = 8  # number of nearest neighbors
                        nearest = (-sim[i, :]).argsort()[1:top_k + 1]
                        log_str = 'Nearest to %s:' % valid_word
                        for k in range(top_k):
                            close_word = reverse_dictionary[nearest[k]]
                            log_str = '%s %s,' % (log_str, close_word)
                        print(log_str)
            final_embeddings = normalized_embeddings.eval()

            # Write corresponding labels for the embeddings.
            with open(FLAGS.log_dir + '/metadata.tsv', 'w') as f:
                for i in range(vocabulary_size):
                    f.write(reverse_dictionary[i] + '\n')

            # Save the model for checkpoints.
            saver.save(session, os.path.join(FLAGS.log_dir, 'model.ckpt'))

            # Create a configuration for visualizing embeddings with the labels in TensorBoard.
            config = projector.ProjectorConfig()
            embedding_conf = config.embeddings.add()
            embedding_conf.tensor_name = embeddings.name
            embedding_conf.metadata_path = os.path.join(FLAGS.log_dir, 'metadata.tsv')
            projector.visualize_embeddings(writer, config)

    writer.close()
    return final_embeddings


# Step 6: Visualize the embeddings.


# pylint: disable=missing-docstring
# Function to draw visualization of distance between embeddings.
def plot_with_labels(low_dim_embs, labels, filename):
    assert low_dim_embs.shape[0] >= len(labels), 'More labels than embeddings'
    plt.figure(figsize=(18, 18))  # in inches
    for i, label in enumerate(labels):
        x, y = low_dim_embs[i, :]
        plt.scatter(x, y)
        plt.annotate(
            label,
            xy=(x, y),
            xytext=(5, 2),
            textcoords='offset points',
            ha='right',
            va='bottom')

    plt.savefig(filename)


if __name__ == "__main__":
    # Step 1 : Download Data
    # filename = maybe_download('text8.zip', 3144016)
    # vocabulary = read_data(filename)
    print('Data Size : {}'.format(len(vocabulary)))
    # Step 2 : Prepare Data
    # data, count, dictionary, reverse_dictionary = build_dataset(vocabulary, vocabulary_size)
    print('Most common words (+UNK) {}'.format(count[:5]))
    del vocabulary  # Reducing Memory imprint
    # Step 3 : Generate batch & labels
    batch, labels = generate_batch(data, batch_size=8, num_skips=2, skip_window=1)

    # for i in range(8):
    #     print(batch[i], reverse_dictionary[batch[i]], '->', labels[i, 0], reverse_dictionary[labels[i, 0]])
    final_embeddings = build_graph()
    print("Training Completed")

    try:
        # pylint: disable=g-import-not-at-top
        from sklearn.manifold import TSNE
        import matplotlib.pyplot as plt

        tsne = TSNE(
            perplexity=30, n_components=2, init='pca', n_iter=5000, method='exact')
        plot_only = 500
        low_dim_embs = tsne.fit_transform(final_embeddings[:plot_only, :])
        labels = [reverse_dictionary[i] for i in range(plot_only)]
        plot_with_labels(low_dim_embs, labels, os.path.join(os.path.dirname(__file__), 'tsne.png'))

    except ImportError as ex:
        print('Please install sklearn, matplotlib, and scipy to show embeddings.')
        print(ex)
