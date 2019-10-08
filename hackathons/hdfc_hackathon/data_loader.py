"""
Data Loading  and feature engineering module
"""
import os
import pickle

import numpy as np
import pandas as pd
# from imblearn.over_sampling import SMOTE
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler

from common.config_files.config import CGNConfigParser

CONFIG_ALL = CGNConfigParser()
CONFIG = CONFIG_ALL.get_sub_config('hdfc')

def read_csv():
  """
  Loads train and test csv files
  """
  train_df = pd.read_csv(CONFIG['train'])
  test_df = pd.read_csv(CONFIG['test'])
  return train_df, test_df


def feature_importance(df, threshold=0.7):
  """[summary]

  Args:
      df ([type]): [description]
      threshold (float, optional): [description]. Defaults to 0.7.

  Returns:
      [type]: [description]
  """

  # Feature Importance Filtering
  feature_imp = pd.read_csv(CONFIG['feature_imp_path'])
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
  """[summary]

  Args:
      train_df ([type]): [description]
      orig_train_df ([type]): [description]
      test_df ([type]): [description]
      columns ([type], optional): [description]. Defaults to None.
      columns_path (str, optional): [description]. Defaults to 'columns.pickle'.

  Returns:
      [type]: [description]
  """

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
  """[summary]

  Args:
      labels ([type]): [description]
  """
  neg, pos = np.bincount(labels)

  total = neg + pos
  print(
    '{} positive samples out of {} training samples ({:.2f}% of total)'.format(
      pos, total, 100 * pos / total))


def simple_imputation(df_train, df_test, strategy="most_frequent"):
  """[summary]


  Args:
      df_train ([type]): [description]
      df_test ([type]): [description]
      strategy ([type]): [description]
      strategy supported
      "mean" : average
      "median" : med
      "most frequent" : mode
      Logic, input train and test. Append them and then do imputation

  Returns:
      [type]: [description]
  """
  ##imputer is fitted on both train and test. remove ".append(df_test)" to fit on only train
  df = df_train.append(df_test)
  imputer = SimpleImputer(missing_values=np.nan, strategy=strategy)
  imputer = imputer.fit(df)
  col_list = df.columns
  df_train_imputed = pd.DataFrame(
    imputer.transform(df_train),
    columns=[str(col) + '_' + strategy for col in col_list])
  df_test_imputed = pd.DataFrame(
    imputer.transform(df_test),
    columns=[str(col) + '_' + strategy for col in col_list])
  return df_train_imputed, df_test_imputed


def drop_columns(df, missing_col):
  """
  drops columns from a database
  """
  df = df.drop(missing_col, axis=1)
  return df

def get_null_columns(train, null_threshold=0.4):
  """
  finds columns with null values greater than threshold(default=0.4)
  returns list of columns to be removed
  """
  missingcol = train.columns[(
      train.isnull().sum()/train.shape[0]) > null_threshold]
  return missingcol

def get_scaled_data(train, test):
  """
  Scale train and test data using MinMaxScaler
  """
  min_max_scaler = MinMaxScaler()
  min_max_scaler.fit(train)
  x_train_scaled = min_max_scaler.transform(train)
  x_test_scaled = min_max_scaler.transform(test)
  return x_train_scaled, x_test_scaled

def get_correlated_cols(train, threshold=0.7):
  """
  gets a random column from a pair of columns with correlation greater than some threshold
  """
  corr_matrix = train.corr().abs()
  upper = corr_matrix.where(
      np.triu(np.ones(corr_matrix.shape), k=1).astype(np.bool))
  to_drop = [column for column in upper.columns if any(
      upper[column] > threshold)]
  return to_drop

def load_data():
  """
  main function for loading data
  returns direct input for training
  """
  target_col = 'Col2'
  corr_threshold = 0.7
  train, test = read_csv()
  x_train = train.loc[:, train.columns != target_col]
  y_train = train.loc[:, train.columns == target_col]
  x_test = test.loc[:, test.columns != target_col]
  missing_col = get_null_columns(x_train)
  x_train = drop_columns(x_train, missing_col)
  x_test = drop_columns(x_test, missing_col)
  x_train, x_test = simple_imputation(x_train, x_test)
  x_train, x_test = get_scaled_data(x_train, x_test)
  correlated_cols = get_correlated_cols(x_train, corr_threshold)
  x_train = drop_columns(x_train, correlated_cols)
  x_test = drop_columns(x_test, correlated_cols)
  return x_train, y_train, x_test, test
