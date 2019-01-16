from utility import cifar10
from utility.cifar10 import img_size
import sys
import os
import tensorflow as tf
from datetime import datetime
LOGDIR = os.path.join(os.getcwd(),'log')
DATASET='cifar10_cnn'
LOGDIR_EVAL = os.path.join(os.getcwd(),'log_eval')
DATADIR =  os.path.join(os.getcwd(),'data')
MODELDIR = os.path.join(os.getcwd(),'model')
TIMESTAMP=datetime.now().strftime('%Y-%m-%d_%H_%M')

INPUT = 32
HIDDEN_LAYER1= 8
HIDDEN_LAYER2 = 16
HIDDEN_LAYER3=32
OUTPUT = INPUT

def prepare_data():
    cifar10.maybe_download_and_extract()
    images_train, cls_train, labels_train = cifar10.load_training_data()
    images_test, cls_test, labels_test = cifar10.load_test_data()
    print("Size of:")
    print("- Training-set:\t\t{}".format(len(images_train)))
    print("- Test-set:\t\t{}".format(len(images_test)))
    return images_train,images_test


def weight_init(shape,name):
   # weight = tf.get_variable(name=name,dtype=tf.float32,shape=shape,initializer=tf.contrib.layers.variance_scaling_initializer())
    weight = tf.Variable(tf.truncated_normal(shape, stddev=0.1))
    return weight

def bias_init(shape,name):
    bias = tf.get_variable(name=name,dtype=tf.float32,shape=shape,initializer=tf.contrib.layers.variance_scaling_initializer())
    return bias

def autoencoder(x,type='stacked',layer=2,activation=tf.nn.relu,regularization=tf.contrib.layers.l2_regularizer(0.0001)):
    x_image = tf.reshape(x, [-1, 32, 32, 3])
    tf.summary.image('input', x_image, 3)
    print(x.shape)

    #Layer 1 : Input X HIDDEN_LAYER1
    #INPUT - 32 X 32 X 3 | OUTPUT - 16 X 16 X 8
    with tf.name_scope('Layer_1'):
        weight1 = weight_init([5,5,3,HIDDEN_LAYER1], name='weight1')
        #bias1 = bias_init([HIDDEN_LAYER1], name='bias1')
        l1 = tf.nn.conv2d(x,filter=weight1,strides=(1,2,2,1),padding='SAME')
        tf.summary.histogram("layer1", l1)
        tf.summary.histogram("weight1", weight1)
        # tf.summary.histogram("bias1", bias1)

    # Layer 2 : HIDDEN_LAYER1 X HIDDEN_LAYER2
    # INPUT - 16 X 16 X 8 | OUTPUT - 8 X 8 X 16
    with tf.name_scope('Layer_2'):
        weight2 = weight_init([5,5,HIDDEN_LAYER1, HIDDEN_LAYER2], name='weight2')
        # bias2 = bias_init([HIDDEN_LAYER2], name='bias2')
        l2 = tf.nn.conv2d(l1,filter=weight2,strides=(1,2,2,1),padding='SAME')
        tf.summary.histogram("layer2", l2)
        tf.summary.histogram("weight2", weight2)
        # tf.summary.histogram("bias2", bias2)

    # if not type=='stacked':
    #     weight3 = tf.transpose(weight2,name='weight3')
    #     weight4 = tf.transpose(weight1,name='weight4')
    # else:
    #     weight3 = weight_init([HIDDEN_LAYER2, HIDDEN_LAYER1], name='weight3')
    #     weight4 = weight_init([HIDDEN_LAYER1, OUTPUT], name='weight4')

    # Layer 3 : HIDDEN_LAYER2 X HIDDEN_LAYER3'
    # INPUT - 8 X 8 X 16 | OUTPUT - 2 X 2 X 32
    # Latent Encoded Layer : reduction from (32x32x3) [3072] to (2x2x32) [128]
    with tf.name_scope('Encoding_Layer_3'):
        weight3 = weight_init([5,5,HIDDEN_LAYER2, HIDDEN_LAYER3], name='weight3')
        #bias3 = bias_init([HIDDEN_LAYER1], name='bias3')
        l3 = tf.nn.conv2d(l2, filter=weight3, strides=(1,4, 4,1), padding='SAME')
        # print("-----------l3 ", l3.shape)
        tf.summary.histogram("layer3", l3)
        tf.summary.histogram("weight3", weight3)
        # tf.summary.histogram("bias3", bias3)

    # Decoder Layers

    # Layer 4 : HIDDEN_LAYER2 X HIDDEN_LAYER3'
    # INPUT - 2 X 2 X 32 | OUTPUT - 8 X 8 X 32
    with tf.name_scope('Layer_4'):
        #weight4 = weight_init([5,5,HIDDEN_LAYER3, HIDDEN_LAYER3], name='weight4')
        # bias4 = bias_init([OUTPUT], name='bias4')
        l4 = tf.layers.conv2d_transpose(l3,filters=32,kernel_size=[5,5] ,strides=(4, 4), padding='SAME')
        # print("-----------l4 ",l4.shape)
        tf.summary.histogram("layer4", l4)
        # tf.summary.histogram("weight4", weight4)
        # tf.summary.histogram("bias4", bias4)
        # x_eval_image = tf.reshape(out, [-1, 32, 32, 1])
        # tf.summary.image('reconstructed', x_eval_image, 3)

    # Layer 5 : HIDDEN_LAYER2 X HIDDEN_LAYER3'
    # INPUT - 8 X 8 X 32 | OUTPUT - 16 X 16 X 16
    with tf.name_scope('Layer_5'):
        #weight5 = weight_init([5, 5, HIDDEN_LAYER2, HIDDEN_LAYER3], name='weight4')
        # bias4 = bias_init([OUTPUT], name='bias4')
        l5 = tf.layers.conv2d_transpose(l4, filters=16,kernel_size=[5,5], strides=(2, 2), padding='SAME')
        # print("-----------l5 ", l5.shape)
        tf.summary.histogram("layer5", l5)
        #tf.summary.histogram("weight4", weight5)
        # tf.summary.histogram("bias4", bias4)

    # Layer 6 : HIDDEN_LAYER2 X HIDDEN_LAYER3'
    # INPUT - 16 X 16 X 16 | OUTPUT - 32 X 32 X 3
    with tf.name_scope('Layer_6'):
        # weight6 = weight_init([5, 5, 3, HIDDEN_LAYER2], name='weight1')
        # bias1 = bias_init([HIDDEN_LAYER1], name='bias1')
        l6 = tf.layers.conv2d_transpose(l5, filters=3,kernel_size=[5,5], strides=(2, 2), padding='SAME')
        # print("-----------l6 ", l6.shape)
        tf.summary.histogram("layer6", l6)
        # tf.summary.histogram("weight1", weight1)
        # tf.summary.histogram("bias1", bias1)

    with tf.name_scope('Output_layer'):
        output = tf.identity(l6, name="encoded_representation")  # the latent representation of the input image.
        # print("-----------output ", output.shape)
        x_eval_image = tf.reshape(output, [-1, 32, 32, 3])
        tf.summary.image('reconstructed', x_eval_image, 3)

    #Loss
    with tf.name_scope('Loss'):
        #loss = tf.sqrt(tf.reduce_mean(tf.square(output - x)), name="loss")
        loss = tf.reduce_mean(tf.squared_difference(output,x))
        # regularization_loss = regularization(weight1) + regularization(weight2)
        # if type == 'stacked':
        #     regularization_loss += regularization(weight3) + regularization(weight4)
        # loss = reconstruction_loss + regularization_loss

    return loss,output,l3,x_image



def create_summaries(loss, x, latent, output,type='stacked'):
    writer = tf.summary.FileWriter(os.path.join(LOGDIR,DATASET,type+'_'+TIMESTAMP))
    writer1 = tf.summary.FileWriter(os.path.join(LOGDIR,DATASET,type+'_eval_' + TIMESTAMP))
    tf.summary.scalar("Loss", loss)
    return writer,writer1,tf.summary.merge_all()

def main():
    type='stacked'
    #Get Data
    cifar_train, cifar_test = prepare_data()
    # print(cifar_train.shape)
    #cifar_train_reshaped = cifar_train.reshape(10000,-1)
    #cifar_train_reshaped = tf.reshape(cifar_train,shape=(50,-1))
    #Placeholder for data
    x = tf.placeholder(tf.float32,shape=(None,32,32,3))
    #test = tf.placeholder(tf.int8,shape=[1])

    #Auto Encoder
    loss , output ,encoding,x_image = autoencoder(x=x)

    #Training Step
    train_step = tf.train.AdamOptimizer(0.005).minimize(loss)

    # We want to use Tensorboard to visualize some stuff
    writer, writer1,summary_op = create_summaries(loss, x, encoding, output)
    saver = tf.train.Saver()
    #Start Training
    n_epoch = 50
    batch_size = 1000
    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())
        writer.add_graph(sess.graph)

        for epoch in range(n_epoch):
            # print("Here ... ")
            n_batches = cifar_train.shape[0] // batch_size
            # print(cifar_train.shape[0])
            #n_batches = n_batches_dimension.value
            idx=0
            for iteration in range(n_batches):
                print("\r{}%".format(100 * iteration // n_batches), end="")  # not shown in the book
                sys.stdout.flush()
                #print("idx : {} - n_batches : {}".format(idx,n_batches))
                X_batch = cifar_train[idx:idx+batch_size]
                #X = X_batch.eval()
                #print(X_batch.shape)
                idx +=batch_size
                if iteration % 10 == 0:
                    _, s = sess.run([train_step, summary_op], feed_dict={x: X_batch})
                    writer.add_summary(s, iteration)
            loss_train = loss.eval(feed_dict={x: X_batch})
            print("\r{}".format(epoch), "Train MSE:", loss_train)  # not shown
        model_path = os.path.join(MODELDIR,DATASET,DATASET+'_'+type+'_'+TIMESTAMP)
        if not os.path.exists(model_path):
            os.makedirs(model_path)
        saver.save(sess, os.path.join(model_path, "my_model_all_layers.ckpt"))
        X_test = cifar_test[0:5]
        #X_test = sample_test.reshape(sample_test.shape[0],32,32,3)
        # # evalaution
        _, sum1 = sess.run([x_image, summary_op], feed_dict={x: X_test})
        _, sum2 = sess.run([output, summary_op], feed_dict={x: X_test})
        writer1.add_summary(sum1)
        writer1.add_summary(sum2)


if __name__ == '__main__':
    main()
    #prepare_data()