from utility import cifar10
from utility.cifar10 import img_size
import tensorflow as tf

def prepare_train_data():
    cifar10.maybe_download_and_extract()
    images_train, cls_train, labels_train = cifar10.load_training_data()
    print("Size of:")
    print("- Training-set:\t\t{}".format(len(images_train)))
    return images_train, cls_train, labels_train


def prepare_test_data():
    cifar10.maybe_download_and_extract()

    images_test, cls_test, labels_test = cifar10.load_test_data()
    print("Size of:")
    print("- Test-set:\t\t{}".format(len(images_test)))
    return images_test, cls_test, labels_test

def weight_init(shape,name):
    weight = tf.get_variable(name=name,dtype=tf.float32,shape=shape,initializer=tf.contrib.layers.variance_scaling_initializer())
    return weight

def bias_init(shape,name):
    bias = tf.get_variable(name=name,dtype=tf.float32,shape=shape,initializer=tf.contrib.layers.variance_scaling_initializer())
    return bias

def single_layer(X,Y_):
    weight1 = weight_init([3072, 10], name='weight1')
    bias1 = bias_init([10], name='bias1')
    XX = tf.reshape(X, [-1, 3072])
    activation = tf.matmul(XX,weight1) + bias1
    Y = tf.nn.softmax(activation)
    loss = -tf.reduce_mean(Y_ * tf.log(Y + 1e-15)) * 1000.0

    return weight1,loss

def main():
    #Get Data
    images_train, cls_train, labels_train = prepare_train_data()
    images_test, cls_test, labels_test=prepare_test_data()

    # input X: 28x28 grayscale images, the first dimension (None) will index the images in the mini-batch
    X = tf.placeholder(tf.float32,shape=[None,32,32,3])
    # correct answers will go here
    Y_ = tf.placeholder(tf.float32, [None, 10])

    n_epoch = 1
    batch_size = 100

    weight1,loss = single_layer(X,Y_)
    # training, learning rate = 0.005
    train_step = tf.train.GradientDescentOptimizer(0.005).minimize(loss)

    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())
        for epoch in range(n_epoch):
            n_batches = images_train.shape[0] // batch_size
            # n_batches = n_batches_dimension.value
            idx = 0
            for iteration in range(n_batches):
                X_batch = images_train[idx:idx + batch_size]
                Y_batch = labels_train[idx:idx + batch_size]
                idx += batch_size
                print("\r{}%".format(100 * iteration // n_batches), end="")  # not shown in the book
                # sys.stdout.flush()
                sess.run(train_step, feed_dict={X: X_batch, Y_: Y_batch})
            w = weight1.eval()
            loss_train = loss.eval(feed_dict={X: X_batch, Y_: Y_batch})
            #print("\r{}".format(epoch), "W", w)
            # print("\r{}".format(epoch), "reshaped", xx)
            # print("\r{}".format(epoch), "activation", a)  # not shown
            # print("\r{}".format(epoch), "Y", y)  # not shown
            print("\r{}".format(epoch), "Train MSE:", loss_train)  # not shown

if __name__ == '__main__':
    main()

