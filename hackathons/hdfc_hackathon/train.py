import os
import pickle

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import tensorflow as tf
from sklearn import metrics
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from tensorflow import keras

# from imblearn.over_sampling import SMOTE
import models
import evaluation
import data_loader
from common.config_files.config import CGNConfigParser


def train_neural_network():

  train_df, orig_test_df, test_df = data_loader.read_csv()
  train_features, train_labels, test_features = data_loader.feature_filtering(
    train_df, orig_test_df, test_df)

  model = models.make_model(features=train_features)

  checkpoint_cb, tensorboard_cb = models.callbacks(
    model_name='nn_submission03_s_1_m1_f_2165.ckpt')
  EPOCHS = 1
  BATCH_SIZE = 32

  history = model.fit(train_features,
                      train_labels,
                      batch_size=BATCH_SIZE,
                      epochs=EPOCHS,
                      callbacks=[checkpoint_cb, tensorboard_cb]
                      #     validation_data=(val_features, val_labels)
                     )

  evaluation.evaluation(model, train_features, train_labels)
  evaluation.plot_metrices(EPOCHS, history, if_val=False)
  evaluation.plot_confusion_matrix(model, train_features, train_labels)
  evaluation.submission(model=model,
                        test_features=test_features,
                        orig_test_df=orig_test_df,
                        submission_name='nn_submission03_s_1_m1_f_2165.csv')


def train_lightgbm():
  """
  read imputed features
  trains NUM light gbm model and saves to an pickle object
  call submission_lgbm to predict and create submission dataframe
  """
  train_df, orig_test_df, test_df = data_loader.read_csv()
  train_features, train_labels, test_features = data_loader.feature_filtering(
    train_df, orig_test_df, test_df)
  num_lgbm_ensemble = 17
  lgb_forests = []
  for i in range(num_lgbm_ensemble):
    print("training LGBC model {}".format(i))
    n_estimators = 900
    max_depth = 7
    learning_rate = 0.01
    random_state = i
    colsample_bytree = 0.1
    reg_lambda = 15
    reg_alpha = 10
    lgbc = models.make_model_lgbm(n_estimators, max_depth, learning_rate, i,
                                  colsample_bytree, reg_lambda, reg_alpha)
    lgbc.fit(train_features, train_labels)
    lgb_forests.append(lgbc)

  config_all = CGNConfigParser()
  config = config_all.get_sub_config('hdfc')
  model_path = config['model_path']
  model_file_path = os.path.join(model_path, "lgb", "lgb_forest.pkl")
  pickle.dump(lgb_forests, open(model_file_path, 'wb'))

  evaluation.submission_lgbm(model_file_path,
                             test_features,
                             orig_test_df,
                             submission_name='submission_lgb.csv')


if __name__ == "__main__":
  train_neural_network()
  train_lightgbm()