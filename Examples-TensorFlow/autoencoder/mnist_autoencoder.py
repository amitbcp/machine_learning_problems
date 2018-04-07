import sys
import os
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
from datetime import datetime

LOGDIR = os.path.join(os.getcwd(),'log')
LOGDIR_EVAL = os.path.join(os.getcwd(),'log_eval')
DATADIR =  os.path.join(os.getcwd(),'data')
MODELDIR = os.path.join(os.getcwd(),'model')
TIMESTAMP=datetime.now().strftime('%Y-%m-%d_%H_%M')

INPUT = 784
HIDDEN_LAYER1= 300
HIDDEN_LAYER2 = 150
HIDDEN_LAYER3=300
OUTPUT = 784

def weight_init(shape,name):
    weight = tf.get_variable(name=name,dtype=tf.float64,shape=shape,initializer=tf.contrib.layers.variance_scaling_initializer())
    return weight

def bias_init(shape,name):
    bias = tf.get_variable(name=name,dtype=tf.float64,shape=shape,initializer=tf.contrib.layers.variance_scaling_initializer())
    return bias

def autoencoder(x,test,type='stacked',layer=2,activation=tf.nn.relu,regularization=tf.contrib.layers.l2_regularizer(0.0001)):
    x_image = tf.reshape(x, [-1, 28, 28, 1])
    tf.summary.image('input', x_image, 3)

    #Layer 1 : Input X HIDDEN_LAYER1
    with tf.name_scope('Layer_1'):
        weight1 = weight_init([INPUT, HIDDEN_LAYER1], name='weight1')
        bias1 = bias_init([HIDDEN_LAYER1], name='bias1')
        #l1 = tf.matmul(x,weight1)+bias1
        l1 = activation(tf.matmul(x,weight1)+bias1)
        tf.summary.histogram("layer1", l1)
        tf.summary.histogram("weight1", weight1)
        tf.summary.histogram("bias1", bias1)

    # Layer 2 : HIDDEN_LAYER1 X HIDDEN_LAYER2
    with tf.name_scope('Layer_2'):
        weight2 = weight_init([HIDDEN_LAYER1, HIDDEN_LAYER2], name='weight2')
        bias2 = bias_init([HIDDEN_LAYER2], name='bias2')
        l2 = activation(tf.matmul(l1, weight2) + bias2)
        tf.summary.histogram("layer2", l2)
        tf.summary.histogram("weight2", weight2)
        tf.summary.histogram("bias2", bias2)

    if not type=='stacked':
        weight3 = tf.transpose(weight2,name='weight3')
        weight4 = tf.transpose(weight1,name='weight4')
    else:
        weight3 = weight_init([HIDDEN_LAYER2, HIDDEN_LAYER1], name='weight3')
        weight4 = weight_init([HIDDEN_LAYER1, OUTPUT], name='weight4')

    # Layer 3 : HIDDEN_LAYER2 X HIDDEN_LAYER3'
    with tf.name_scope('Layer_3'):
        bias3 = bias_init([HIDDEN_LAYER1], name='bias3')
        l3 = activation(tf.matmul(l2, weight3) + bias3)
        tf.summary.histogram("layer3", l3)
        tf.summary.histogram("weight3", weight3)
        tf.summary.histogram("bias3", bias3)

    # Layer 4/OutPut Layer : HIDDEN_LAYER3 X OUTPUT
    with tf.name_scope('Output_Layer'):
        bias4 = bias_init([OUTPUT], name='bias4')
        out = tf.matmul(l3, weight4) + bias4
        tf.summary.histogram("output", out)
        tf.summary.histogram("weight4", weight4)
        tf.summary.histogram("bias4", bias4)
        x_eval_image = tf.reshape(out, [-1, 28, 28, 1])
        tf.summary.image('reconstructed', x_eval_image, 3)




    #Loss
    with tf.name_scope('Loss'):
        reconstruction_loss = tf.reduce_mean(tf.squared_difference(out,x))
        regularization_loss = regularization(weight1) + regularization(weight2)
        # if type == 'stacked':
        #     regularization_loss += regularization(weight3) + regularization(weight4)
        loss = reconstruction_loss + regularization_loss

    return loss,out,l2,x_image



def create_summaries(loss, x, latent, output,type='stacked'):
    writer = tf.summary.FileWriter(os.path.join(LOGDIR,type+'_'+TIMESTAMP))
    writer1 = tf.summary.FileWriter(os.path.join(LOGDIR,type+'_eval_' + TIMESTAMP))
    tf.summary.scalar("Loss", loss)
    return writer,writer1,tf.summary.merge_all()



def main():
    type='stacked'
    #Get Data
    mnist = input_data.read_data_sets(os.path.join(DATADIR,'mnist'))
    #Placeholder for data
    x = tf.placeholder(tf.float64,shape=[None,784])
    test = tf.placeholder(tf.int8,shape=[1])

    #Auto Encoder
    loss , output ,encoding,x_image = autoencoder(x=x,test=test)

    #Training Step
    train_step = tf.train.AdamOptimizer(0.005).minimize(loss)

    # We want to use Tensorboard to visualize some stuff
    writer, writer1,summary_op = create_summaries(loss, x, encoding, output)
    saver = tf.train.Saver()
    #Start Training
    n_epoch = 30
    batch_size = 100
    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())
        writer.add_graph(sess.graph)

        for epoch in range(n_epoch):
            n_batches = mnist.train.num_examples // batch_size
            for iteration in range(n_batches):
                print("\r{}%".format(100 * iteration // n_batches), end="")  # not shown in the book
                sys.stdout.flush()
                X_batch, Y_batch = mnist.train.next_batch(batch_size)
                if iteration % 5 == 0:
                    _, s = sess.run([train_step, summary_op], feed_dict={x: X_batch})
                    writer.add_summary(s, iteration)
            loss_train = loss.eval(feed_dict={x: X_batch})
            print("\r{}".format(epoch), "Train MSE:", loss_train)  # not shown
        model_path = os.path.join(MODELDIR,type+'_'+TIMESTAMP)
        if not os.path.exists(model_path):
            os.mkdir(model_path)
        saver.save(sess, os.path.join(model_path, "my_model_all_layers.ckpt"))
        X_test = mnist.test.images[0:5]
        # evalaution
        _, sum1 = sess.run([x_image, summary_op], feed_dict={x: X_test})
        _, sum2 = sess.run([output, summary_op], feed_dict={x: X_test})
        writer1.add_summary(sum1)
        writer1.add_summary(sum2)

if __name__=='__main__':
    main()
