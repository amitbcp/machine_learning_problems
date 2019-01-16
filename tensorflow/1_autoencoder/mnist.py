#!/usr/bin/env python

"""TensorFlow MNIST AutoEncoder

This is my attempt to write the autoencoder for MNIST by Andrej Karpathy using
ConvNetJS in TensorFlow. Mostly to get some more experience working in
Tensorflow.

Sources:
    - http://cs.stanford.edu/people/karpathy/convnetjs/demo/autoencoder.html
    - https://www.tensorflow.org/get_started/mnist/pros

Author: Gertjan van den Burg
Date: Thu Oct 26 16:49:29 CEST 2017

"""

import numpy as np
import tensorflow as tf

from magenta.models.image_stylization.image_utils import form_image_grid
from tensorflow.examples.tutorials.mnist import input_data

BATCH_SIZE = 50
GRID_ROWS = 5
GRID_COLS = 10
USE_RELU = False


def weight_variable(shape):
    # From the mnist tutorial
    initial = tf.truncated_normal(shape, stddev=0.1)
    return tf.Variable(initial)


def bias_variable(shape):
    initial = tf.constant(0.1, shape=shape)
    return tf.Variable(initial)


def fc_layer(previous, input_size, output_size):
    W = weight_variable([input_size, output_size])
    b = bias_variable([output_size])
    return tf.matmul(previous, W) + b


def autoencoder(x):
    # first fully connected layer with 50 neurons using tanh activation
    l1 = tf.nn.tanh(fc_layer(x, 28*28, 50))
    # second fully connected layer with 50 neurons using tanh activation
    l2 = tf.nn.tanh(fc_layer(l1, 50, 50))
    # third fully connected layer with 2 neurons
    l3 = fc_layer(l2, 50, 2)
    # fourth fully connected layer with 50 neurons and tanh activation
    l4 = tf.nn.tanh(fc_layer(l3, 2, 50))
    # fifth fully connected layer with 50 neurons and tanh activation
    l5 = tf.nn.tanh(fc_layer(l4, 50, 50))
    # readout layer
    if USE_RELU:
        out = tf.nn.relu(fc_layer(l5, 50, 28*28))
    else:
        out = fc_layer(l5, 50, 28*28)
    # let's use an l2 loss on the output image
    loss = tf.reduce_mean(tf.squared_difference(x, out))
    return loss, out, l3


def layer_grid_summary(name, var, image_dims):
    prod = np.prod(image_dims)
    grid = form_image_grid(tf.reshape(var, [BATCH_SIZE, prod]), [GRID_ROWS,
        GRID_COLS], image_dims, 1)
    return tf.summary.image(name, grid)


def create_summaries(loss, x, latent, output):
    writer = tf.summary.FileWriter("./logs")
    tf.summary.scalar("Loss", loss)
    layer_grid_summary("Input", x, [28, 28])
    layer_grid_summary("Encoder", latent, [2, 1])
    layer_grid_summary("Output", output, [28, 28])
    return writer, tf.summary.merge_all()


def make_image(name, var, image_dims):
    prod = np.prod(image_dims)
    grid = form_image_grid(tf.reshape(var, [BATCH_SIZE, prod]), [GRID_ROWS,
        GRID_COLS], image_dims, 1)
    s_grid = tf.squeeze(grid, axis=0)

    # This reproduces the code in: tensorflow/core/kernels/summary_image_op.cc
    im_min = tf.reduce_min(s_grid)
    im_max = tf.reduce_max(s_grid)

    kZeroThreshold = tf.constant(1e-6)
    max_val = tf.maximum(tf.abs(im_min), tf.abs(im_max))

    offset = tf.cond(
            im_min < tf.constant(0.0),
            lambda: tf.constant(128.0),
            lambda: tf.constant(0.0)
            )
    scale = tf.cond(
            im_min < tf.constant(0.0),
            lambda: tf.cond(
                max_val < kZeroThreshold,
                lambda: tf.constant(0.0),
                lambda: tf.div(127.0, max_val)
                ),
            lambda: tf.cond(
                im_max < kZeroThreshold,
                lambda: tf.constant(0.0),
                lambda: tf.div(255.0, im_max)
                )
            )
    s_grid = tf.cast(tf.add(tf.multiply(s_grid, scale), offset), tf.uint8)
    enc = tf.image.encode_jpeg(s_grid)

    fwrite = tf.write_file(name, enc)
    return fwrite


def main():
    # initialize the data
    mnist = input_data.read_data_sets('/tmp/MNIST_data')

    # placeholders for the images
    x = tf.placeholder(tf.float32, shape=[None, 784])

    # build the model
    loss, output, latent = autoencoder(x)

    # and we use the Adam Optimizer for training
    train_step = tf.train.AdamOptimizer(1e-4).minimize(loss)

    # We want to use Tensorboard to visualize some stuff
    writer, summary_op = create_summaries(loss, x, latent, output)

    first_batch = mnist.train.next_batch(BATCH_SIZE)

    # Run the training loop
    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())
        sess.run(make_image("images/input.jpg", x, [28, 28]), feed_dict={x :
            first_batch[0]})
        for i in range(int(200001)):
            batch = mnist.train.next_batch(BATCH_SIZE)
            feed = {x : batch[0]}
            if i % 500 == 0:
                summary, train_loss = sess.run([summary_op, loss],
                        feed_dict=feed)
                print("step %d, training loss: %g" % (i, train_loss))

                writer.add_summary(summary, i)
                writer.flush()

            if i % 1000 == 0:
                sess.run(make_image("images/output_%06i.jpg" % i, output, [28,
                    28]), feed_dict={x : first_batch[0]})

            train_step.run(feed_dict=feed)

        # Save latent space
        pred = sess.run(latent, feed_dict={x : mnist.test._images})
        pred = np.asarray(pred)
        pred = np.reshape(pred, (mnist.test._num_examples, 2))
        labels = np.reshape(mnist.test._labels, (mnist.test._num_examples, 1))
        pred = np.hstack((pred, labels))
        if USE_RELU:
            fname = "latent_relu.csv"
        else:
            fname = "latent_default.csv"
        np.savetxt(fname, pred)


if __name__ == '__main__':
    main()