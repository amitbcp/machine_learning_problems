"""
Main File
"""
import os
import pickle

import numpy as np
import pandas as pd
from xgboost import XGBClassifier
# from imblearn.over_sampling import SMOTE
import models
import evaluation
import data_loader
from common.config_files.config import CGNConfigParser

CONFIG_ALL = CGNConfigParser()
CONFIG = CONFIG_ALL.get_sub_config('hdfc')
MODEL_PATH = CONFIG['model_path']


def train_neural_network(x_train, train_labels, x_test, orig_test):
  """
  Trains neural network ready-to-use dataframes
  Args:
  X_train: train dataset
  train_labels: train labels
  X_test: test dataset
  """
  train_features = np.array(x_train)
  test_features = np.array(x_test)
  train_labels = np.array(train_labels['Col2'])

  model = models.make_model(params=train_features,
                            model_name='neural_network_1')

  checkpoint_cb, tensorboard_cb = models.callbacks(
    model_name='nn_submission03_s_1_m1_f_2165.ckpt')
  epochs = 6
  batch_size = 32

  history = model.fit(train_features,
                      train_labels,
                      batch_size=batch_size,
                      epochs=epochs,
                      callbacks=[checkpoint_cb, tensorboard_cb]
                      #     validation_data=(val_features, val_labels)
                     )

  evaluation.evaluation(model, train_features, train_labels)
  evaluation.plot_metrices(epochs, history, if_val=False)
  evaluation.plot_confusion_matrix(model, train_features, train_labels)
  evaluation.submission_nn(model=model,
                           test_features=test_features,
                           orig_test_df=orig_test,
                           submission_name='nn_submission03_s_1_m1_f_2165.csv')


def train_lightgbm(x_train, train_labels, x_test, orig_test):
  """
  read imputed features
  trains NUM light gbm model and saves to an pickle object
  call submission_lgbm to predict and create submission dataframe
  """
  train_labels = train_labels['Col2']
  num_lgbm_ensemble = 17
  lgb_forests = []
  for i in range(num_lgbm_ensemble):
    print("training LGBC model {}".format(i))
    params = {
      'n_estimators': 17,
      'max_depth': 7,
      'learning_rate': 0.01,
      'random_state': i,
      'colsample_bytree': 0.1,
      'reg_lambda': 15,
      'reg_alpha': 10
    }

    lgbc = models.make_model(params=params, model_name='light_gbm')
    lgbc.fit(x_train, train_labels)
    lgb_forests.append(lgbc)

  model_file_path = os.path.join(MODEL_PATH, "lgb", "lgb_forest.pkl")
  pickle.dump(lgb_forests, open(model_file_path, 'wb'))

  evaluation.submission_lgbm(model_file_path,
                             x_test,
                             orig_test,
                             submission_name='submission_lgb.csv')


def train_xg_boost(x_train, train_labels, x_test, orig_test):
  train_labels = train_labels['Col2']
  n_estimators = 2
  max_depth = 2
  params = {'n_estimators': n_estimators, 'max_depth': max_depth}
  xgb = models.make_model(params, model_name='xg_boost')
  model_file_path = os.path.join(MODEL_PATH, "xgb", "xgb.pkl")
  print(model_file_path)
  xgb.fit(x_train, pd.DataFrame(train_labels, columns=['Col2']).values.ravel())
  pickle.dump(xgb, open(model_file_path, 'wb'))
  evaluation.submission_default(xgb,
                                x_test,
                                orig_test,
                                submission_name='submission_xgb.csv')


if __name__ == "__main__":
  X_train, Y_train, X_test, Orig_test = data_loader.load_data()
  # print(Orig_test.shape)
  # train_neural_network(X_train, Y_train, X_test, Orig_test)
  # train_lightgbm(X_train, Y_train, X_test, Orig_test)
  train_xg_boost(X_train, Y_train, X_test, Orig_test)
