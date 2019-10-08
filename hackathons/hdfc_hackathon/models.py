"""
Training models
"""
import os
import time

import numpy as np
import tensorflow as tf
from tensorflow import keras
from sklearn import metrics
import lightgbm as lgb
from xgboost import XGBClassifier

from common.config_files.config import CGNConfigParser
# from imblearn.over_sampling import SMOTE

tf.keras.backend.clear_session()
np.random.seed(42)
tf.random.set_seed(42)

CONFIG_ALL = CGNConfigParser()
CONFIG_GENERAL = CONFIG_ALL.get_sub_config('general')
CONFIG = CONFIG_ALL.get_sub_config('general')
log_path = CONFIG_GENERAL['log_path']
model_path = CONFIG_GENERAL['hackathon']


def get_run_logdir(root_logdir=log_path):
  """[summary]

  Args:
      root_logdir ([type], optional): [description]. Defaults to log_path.

  Returns:
      [type]: [description]
  """
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
  """[summary]

  Returns:
      [type]: [description]
  """
  nn_metrics = [
    keras.metrics.Accuracy(name='accuracy'),
    keras.metrics.TruePositives(name='tp'),
    keras.metrics.FalsePositives(name='fp'),
    keras.metrics.TrueNegatives(name='tn'),
    keras.metrics.FalseNegatives(name='fn'),
    keras.metrics.Precision(name='precision'),
    keras.metrics.Recall(name='recall'),
    keras.metrics.AUC(name='auc')
  ]

  return nn_metrics


NN_METRICS = model_metrics()


def make_model(params, model_name='light_gbm'):

  if model_name == 'light_gbm':
    model = lgb.LGBMClassifier(n_estimators=params['n_estimators'],
                               max_depth=params['max_depth'],
                               learning_rate=params['learning_rate'],
                               random_state=params['random_state'],
                               colsample_bytree=params['colsample_bytree'],
                               reg_lambda=params['reg_lambda'],
                               reg_alpha=params['reg_alpha'])

  elif model_name == 'xg_boost':
    model = XGBClassifier(n_estimators=params['n_estimators'],
                          max_depth=params['max_depth'],
                          verbosity=3)

  elif model_name == 'neural_network_1':
    model = nn_model1(params)

  elif model_name == 'neural_network_2':
    model = nn_model2(params)
  print("model initialized")
  return model


def nn_model1(features, model_name='03_model.ckpt'):

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

  model.compile(optimizer='adam',
                loss='binary_crossentropy',
                metrics=NN_METRICS)

  return model


def nn_model2(features,
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
    keras.layers.Dense(
      512,
      activation=activation,
      kernel_initializer=intializer,
    ),
    keras.layers.Dense(
      256,
      activation=activation,
      kernel_initializer=intializer,
    ),
    keras.layers.Dense(1, activation='sigmoid')
  ])

  model.compile(optimizer='adam',
                loss='binary_crossentropy',
                metrics=NN_METRICS)

  return model