import  os
import os.path
import shutil
import sys
import tensorflow as tf
from functools import partial
from tensorflow.examples.tutorials.mnist import input_data
from datetime import datetime

LOGDIR = os.path.join(os.getcwd(),'log')
LOGDIR_EVAL = os.path.join(os.getcwd(),'log_eval')
DATADIR =  os.path.join(os.getcwd(),'data')
MODELDIR = os.path.join(os.getcwd(),'model')
TIMESTAMP=datetime.now().strftime('%Y-%m-%d_%H_%M')
if not os.path.exists(MODELDIR):
    os.mkdir(MODELDIR)

def autoencoder_model():
    # mnist = tf.contrib.learn.datasets.mnist.read_data_sets(train_dir=DATADIR, one_hot=True)
    mnist = input_data.read_data_sets(DATADIR)
    n_inputs= 28 * 28
    n_hidden1 = 300
    n_hidden2 = 150
    n_hidden3 = n_hidden1
    n_output = n_inputs

    lr = 0.01
    l2_reg = 0.0001

    tf.reset_default_graph()
    sess = tf.Session()

    # Setting up placeholders
    X= tf.placeholder(tf.float32,shape=[None,784],name='X')
    test= tf.placeholder(tf.bool)
    eval=tf.placeholder(tf.bool)

    x_image=tf.reshape(X,[-1,28,28,1])
    tf.summary.image('input', x_image, 3)


    he_init = tf.contrib.layers.variance_scaling_initializer() # He initialization
    l2_regularizer = tf.contrib.layers.l2_regularizer(l2_reg)
    dense_layer = partial(tf.layers.dense,
                          activation=tf.nn.elu,
                          kernel_initializer=he_init,
                          kernel_regularizer = l2_regularizer)

    with tf.name_scope("hidden_layer"):
        hidden1 = dense_layer(X,n_hidden1)
        hidden2 = dense_layer(hidden1, n_hidden2)
        hidden3= dense_layer(hidden2, n_hidden3)
        tf.summary.histogram("hidden_layer1",hidden1)
        tf.summary.histogram("hidden_layer2",hidden2)
        tf.summary.histogram("hidden_layer3",hidden3)

    with tf.name_scope("output_layer"):
        output=dense_layer(hidden3, n_output,activation=None)
        tf.summary.histogram("output", output)

    x_eval_image = tf.reshape(output, [-1, 28, 28, 1])
    tf.summary.image('reconstructed', x_eval_image, 3)



    with tf.name_scope("loss"):
        reconstruction_loss = tf.reduce_mean(tf.square(output-X))
        reg_loss = tf.get_collection(tf.GraphKeys.REGULARIZATION_LOSSES)
        loss = tf.add_n([reconstruction_loss]+reg_loss)

        tf.summary.scalar("reconstruction_loss",reconstruction_loss)
        tf.summary.histogram("regularization_loss",reg_loss)
        tf.summary.scalar("cross_loss",loss)

    with tf.name_scope("train"):
        optimzer = tf.train.AdamOptimizer(lr)
        training_op = optimzer.minimize(loss)
    summ = tf.summary.merge_all()
    init = tf.global_variables_initializer()
    saver = tf.train.Saver()


    n_epoch=5
    batch_size=150

    with tf.Session() as sess:
        init.run()
        writer = tf.summary.FileWriter(os.path.join(LOGDIR,'old',TIMESTAMP))
        writer.add_graph(sess.graph)
        writer1 = tf.summary.FileWriter(os.path.join(LOGDIR_EVAL,'old',TIMESTAMP))
        writer1.add_graph(sess.graph)
        for epoch in range(n_epoch):
            n_batches = mnist.train.num_examples // batch_size
            for iteration in range(n_batches):
                print("\r{}%".format(100 * iteration // n_batches), end="")  # not shown in the book
                sys.stdout.flush()
                X_batch,Y_batch = mnist.train.next_batch(batch_size)
                if iteration % 5 ==0:
                    _,s=sess.run([training_op,summ],feed_dict={X:X_batch,test:False,eval:False})
                    writer.add_summary(s,iteration)

            loss_train = reconstruction_loss.eval(feed_dict={X:X_batch})
            print("\r{}".format(epoch), "Train MSE:", loss_train)  # not shown

            saver.save(sess, os.path.join(MODELDIR,"my_model_all_layers.ckpt"))
        X_test = mnist.test.images[:2]
        # evalaution
        _,sum1 = sess.run([x_image,summ], feed_dict={X: X_test,test:True,eval:False})
        _,sum2 = sess.run([output,summ], feed_dict={X: X_test,test:False,eval:True})
        writer1.add_summary(sum1, 0)
        writer1.add_summary(sum2, 2)
    return mnist




if __name__ == '__main__':
    mnist = autoencoder_model()
    #evaluate_model(mnist)


