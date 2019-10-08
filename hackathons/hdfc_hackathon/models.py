"""
Training models
"""
import os
import time

import numpy as np
import tensorflow as tf
from tensorflow import keras
from sklearn import metrics
from xgboost import XGBClassifier

from common.config_files.config import CGNConfigParser
from utils import model_save
# from imblearn.over_sampling import SMOTE

tf.keras.backend.clear_session()
np.random.seed(42)
tf.random.set_seed(42)
config_all = CGNConfigParser()
config_general = config_all.get_sub_config('general')
config = config_all.get_sub_config('general')
log_path = config_general['log_path']
model_path = config_general['hackathon']
metrics = model_metrics()


def get_run_logdir(root_logdir=log_path):
  run_id = time.strftime("run_%Y_%m_%d-%H_%M_%S")
  print("Log Dir : {}".format(os.path.join(root_logdir, run_id)))
  return os.path.join(root_logdir, run_id)


def callbacks(model_path=model_path, model_name='model.h5'):
  checkpoint_cb = tf.keras.callbacks.ModelCheckpoint(model_path + model_name,
                                                     save_best_only=True)
  run_logdir = get_run_logdir()
  print("Log Dir {}".format(run_logdir))
  tensorboard_cb = tf.keras.callbacks.TensorBoard(run_logdir)

  return checkpoint_cb, tensorboard_cb


def model_metrics():
  metrics = [
    keras.metrics.Accuracy(name='accuracy'),
    keras.metrics.TruePositives(name='tp'),
    keras.metrics.FalsePositives(name='fp'),
    keras.metrics.TrueNegatives(name='tn'),
    keras.metrics.FalseNegatives(name='fn'),
    keras.metrics.Precision(name='precision'),
    keras.metrics.Recall(name='recall'),
    keras.metrics.AUC(name='auc')
  ]

  return metrics


def make_model(features, model_name='03_model.ckpt'):

  #   NN Submission
  model = keras.Sequential([
    keras.layers.Dense(2166,
                       activation="selu",
                       kernel_initializer="lecun_normal",
                       input_shape=(features.shape[-1],)),
    keras.layers.Dense(1024,
                       activation="selu",
                       kernel_initializer="lecun_normal"),
    keras.layers.Dropout(0.3),
    keras.layers.Dense(512,
                       activation="selu",
                       kernel_initializer="lecun_normal"),
    keras.layers.Dropout(0.3),
    keras.layers.Dense(256,
                       activation="selu",
                       kernel_initializer="lecun_normal"),
    keras.layers.Dense(1, activation='sigmoid'),
  ])

  model.compile(optimizer='adam', loss='binary_crossentropy', metrics=metrics)

  return model


def make_model2(features,
                model_name='03_model.ckpt',
                activation='elu',
                intializer='he_normal'):

  #   NN Submission
  model = keras.Sequential([
    keras.layers.Dense(
      2165,
      activation=activation,
      kernel_initializer=intializer,
      #kernel_regularizer=keras.regularizers.l1(0.01),
      input_shape=(features.shape[-1],)),
    keras.layers.Dense(1024,
                       activation=activation,
                       kernel_initializer=intializer),
    #kernel_regularizer=keras.regularizers.l1(0.01)),

    #keras.layers.AlphaDropout(0.6),
    keras.layers.Dense(
      512,
      activation=activation,
      kernel_initializer=intializer,
    ),
    #kernel_regularizer=keras.regularizers.l1(0.01)),

    #keras.layers.AlphaDropout(0.3),
    keras.layers.Dense(
      256,
      activation=activation,
      kernel_initializer=intializer,
    ),
    #kernel_regularizer=keras.regularizers.l1(0.01)),
    keras.layers.Dense(1, activation='sigmoid')
  ])

  model.compile(optimizer='adam', loss='binary_crossentropy', metrics=metrics)

  return model

def xgboost_model(x_train, y_train, params=None):
	"""
	Trains a xgboost model and stores it in a file.

	Args:
		x_train: train dataset.
		y_train: train labels.
		params: input parameters for the model

	Returns:
		Filepath of the model file

	Raises:
		Exception: If dimensions of x_train and y_train donot match
	"""
	xgb_model = XGBClassifier(params)
	xgb_model.fit(x_train, y_train)
	return model_save(xgb_model)
