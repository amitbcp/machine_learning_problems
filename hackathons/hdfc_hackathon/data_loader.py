import os
import pickle

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pickle
import tensorflow as tf
from sklearn import metrics
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from tensorflow import keras
from common.config_files.config import CGNConfigParser
# from imblearn.over_sampling import SMOTE
from sklearn.impute import SimpleImputer
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


def feature_importance(df, threshold=0.7):

  # Feature Importance Filtering
  feature_imp = pd.read_csv(feature_imp_path)
  feature_imp = feature_imp.sort_values(by='imp_score', ascending=False)

  print("Feature Importance from Random Forest {}".format(feature_imp.shape))

  high_imp = feature_imp[feature_imp.imp_score > 0.001]

  # Correleation Matrix to Eliminate Highly Co-related values
  corr_matrix = df.corr().abs()
  upper = corr_matrix.where(
    np.triu(np.ones(corr_matrix.shape), k=1).astype(np.bool))

  to_drop = [
    column for column in upper.columns if any(upper[column] > threshold)
  ]
  print("Rows to drop {}".format(len(to_drop)))
  to_retain = set(df.columns) - set(to_drop)
  print("Rows to retain {}".format(len(to_retain)))

  # Merging both of the above
  final_columns = to_retain.union(set(high_imp['feature_name'].tolist()))
  final_columns = list(final_columns)
  print("Final Number of Features : {}".format(len(final_columns)))

  with open('columns.pickle', 'wb') as f:
    pickle.dump(final_columns, f)

  return final_columns


def feature_filtering(train_df,
                      orig_train_df,
                      test_df,
                      columns=None,
                      columns_path='columns.pickle'):

  if columns is None:
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
# strategy supported
# "mean" : average
# "median" : med
# "most frequent" : mode
# Logic, input train and test. Append them and then do imputation
def mean_simple_imputation(df_train, df_test, strategy):
  df = df_train.append(df_test)
  imputor = SimpleImputer(missing_values=np.nan, strategy=strategy)
  imputor = imputor.fit(df)
  col_list = df.columns
  df_train_scaled = pd.DataFrame(imputor.transform(df_train),
                                 columns=[str(col) + '_'+ strategy for col in col_list.columns])
  df_test_scaled = pd.DataFrame(imputor.transform(df_test),
                                 columns=[str(col) + '_' + strategy for col in col_list.columns])
  return df_train_scaled, df_test_scaled