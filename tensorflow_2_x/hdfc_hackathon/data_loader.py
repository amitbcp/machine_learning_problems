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
from common.config_files.config import CGNConfigParser
# from imblearn.over_sampling import SMOTE

config_all = CGNConfigParser()
config = config_all.get_sub_config('hdfc')


def read_csv():
  train_df = pd.read_csv(config['train_imputed'])
  orig_train_df = pd.read_csv(config['train'])
  train_df.pop('Unnamed: 0')
  train_df.head()

  test_df = pd.read_csv(config['test_imputed'])
  test_df.pop('Unnamed: 0')
  test_df.head()

  return train_df, orig_train_df, test_df


def feature_filtering(train_df, orig_train_df, test_df, columns_path=None):

  if columns_path is None:
    columns = columns = train_df.columns.tolist()
  else:
    with open(columns_path, 'rb') as f:
      columns = pickle.load(f)

  train_features = np.array(train_df[columns])
  train_labels = np.array(orig_train_df['Col2'])

  test_features = np.array(test_df[columns])

  # Normalize the input features using the sklearn StandardScaler.
  # This will set the mean to 0 and standard deviation to 1.
  scaler = StandardScaler()
  train_features = scaler.fit_transform(train_features)
  test_features = scaler.transform(test_features)

  print('Training features shape:', train_features.shape)
  print('Training labels shape:', train_labels.shape)

  print('Test features shape:', test_features.shape)

  return train_features, train_labels, test_features


def sampling(labels):
  neg, pos = np.bincount(labels)

  total = neg + pos
  print(
    '{} positive samples out of {} training samples ({:.2f}% of total)'.format(
      pos, total, 100 * pos / total))
