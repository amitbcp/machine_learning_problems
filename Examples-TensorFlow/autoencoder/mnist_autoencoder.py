import sys
import os
import tensorflow as tf
from functools import partial
from tensorflow.examples.tutorials.mnist import input_data
from datetime import datetime

LOGDIR = os.path.join(os.getcwd(),'log')
LOGDIR_EVAL = os.path.join(os.getcwd(),'log_eval')
DATADIR =  os.path.join(os.getcwd(),'data')
MODELDIR = os.path.join(os.getcwd(),'model')

INPUT = 784
HIDDEN_LAYER1= 300
HIDDEN_LAYER2 = 150
HIDDEN_LAYER3=300
OUTPUT = 784



if not os.path.exists(MODELDIR):
    os.mkdir(MODELDIR)

def weight_init(shape):
    weight = tf.get_variable('W',dtype=tf.float32,shape=shape,initializer=tf.contrib.layers.xavier_initializer(seed=4))
    return weight

def bias_init(shape):
    bias = tf.get_variable('b',dtype=tf.float32,shape=shape,initializer=tf.contrib.layers.xavier_initializer(seed=4))
    return bias
def layer(previous,input_size,output_size,activation=tf.nn.relu):
    weight = weight_init([input_size,output_size])
    b = bias_init[output_size]
    return activation(tf.matmul)
def autoencoder(x,type='stacked',layer=2,activation=tf.nn.relu,regularization=tf.contrib.layers.l2_regularizer(0.01)):

    weight1 = weight_init([INPUT,HIDDEN_LAYER1],name='weight1')
    weight2 = weight_init([HIDDEN_LAYER1,HIDDEN_LAYER2],name='weight2')
    if not type=='stacked':
        weight3 = tf.transpose(weight2,name='weight3')
        weight4 = tf.transpose(weight1,name='weight4')
    else:
        weight3 = weight_init([HIDDEN_LAYER2, HIDDEN_LAYER1], name='weight3')
        weight4 = weight_init([HIDDEN_LAYER1, OUTPUT], name='weight4')


    bias1 = bias_init([HIDDEN_LAYER1], name='bias1')
    bias2 = bias_init([HIDDEN_LAYER2], name='bias2')
    bias3 = bias_init([HIDDEN_LAYER1], name='bias3')
    bias4 = bias_init([HIDDEN_LAYER2], name='bias4')

    #Layer 1 : Input X HIDDEN_LAYER1
    l1 = activation(tf.matmul(x,weight1)+bias1)
    # Layer 2 : HIDDEN_LAYER1 X HIDDEN_LAYER2
    l2 = activation(tf.matmul(l1, weight2) + bias2)
    # Layer 3 : HIDDEN_LAYER2 X HIDDEN_LAYER3
    l3 = activation(tf.matmul(l2, weight3) + bias3)
    # Layer 4/OutPut Layer : HIDDEN_LAYER3 X OUTPUT
    out = tf.matmul(l3, weight4) + bias4

    #Loss
    reconstruction_loss = tf.reduce_mean(tf.squared_difference(out,x))
    regularization_loss = regularization(weight1) + regularization(weight2)
    if type == 'stacked':
        regularization_loss += regularization(weight3) + regularization(weight4)
    loss = reconstruction_loss + regularization_loss

    return loss,out,l2



def create_summaries(loss, x, latent, output):
    writer = tf.summary.FileWriter(os.path.join(LOGDIR,datetime.now().strftime('_%Y-%m-%d_%H:%M:%S')))
    tf.summary.scalar("Loss", loss)
    return writer,tf.summary.merge_all()



def main():
    #Get Data
    mnist = input_data.read_data_sets(os.path.join(DATADIR,'mnist'))
    #Placeholder for data
    x = tf.placeholder(tf.float32,shape=[None,784])

    #Auto Encoder
    loss , output ,encoding = autoencoder(x=x)

    #Training Step
    train_step = tf.train.AdamOptimizer(1e-4).minimize(loss)

    # We want to use Tensorboard to visualize some stuff
    writer, summary_op = create_summaries(loss, x, encoding, output)

    #Start Training
    n_epoch = 5
    batch_size = 150
    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())
        writer.add_graph(sess.graph)

        for epoch in range(n_epoch):
            n_batches = mnist.train.num_examples // batch_size
            for iteration in range(n_batches):







