"""
Model evaluation  module
"""
# from sklearn import metrics
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import utils
import os

from common.config_files.config import CGNConfigParser

CONFIG_ALL = CGNConfigParser()
CONFIG = CONFIG_ALL.get_sub_config('hdfc')
MODEL_PATH = CONFIG['model_path']


# Evaluate baseline Model
def evaluation(model, features, labels):
  results = model.evaluate(features, labels)
  precision = 0
  recall = 0
  for name, value in zip(model.metrics_names, results):
    print(name, ': ', value)

    if name.strip() == 'precision':
      precision = value

    if name.strip() == 'recall':
      recall = value

  if precision != 0 and recall != 0:
    f1 = (2 * precision * recall) / (precision + recall)
    print("F1 : ", f1)


def plot_metrices(EPOCHS, history, if_val=True):

  epochs = range(EPOCHS)

  plt.title('Accuracy')
  plt.plot(epochs, history.history['accuracy'], color='blue', label='Train')
  if if_val:
    plt.plot(epochs,
             history.history['val_accuracy'],
             color='orange',
             label='Val')
  plt.xlabel('Epoch')
  plt.ylabel('Accuracy')
  plt.legend()

  _ = plt.figure()
  plt.title('Loss')
  plt.plot(epochs, history.history['loss'], color='blue', label='Train')
  if if_val:
    plt.plot(epochs, history.history['val_loss'], color='orange', label='Val')
  plt.xlabel('Epoch')
  plt.ylabel('Loss')
  plt.legend()

  _ = plt.figure()
  plt.title('False Negatives')
  plt.plot(epochs, history.history['fn'], color='blue', label='Train')
  if if_val:
    plt.plot(epochs, history.history['val_fn'], color='orange', label='Val')
  plt.xlabel('Epoch')
  plt.ylabel('False Negatives')
  plt.legend()


def plot_confusion_matrix(model, features, labels):
  # Confusion Matrix

  predicted_labels = model.predict(features)
  cm = confusion_matrix(labels, np.round(predicted_labels))

  plt.matshow(cm, alpha=0)
  plt.title('Confusion matrix')
  plt.ylabel('Actual label')
  plt.xlabel('Predicted label')

  for (i, j), z in np.ndenumerate(cm):
    plt.text(j, i, str(z), ha='center', va='center')

  plt.show()

  print('Legitimate Customers Detected (True Negatives): ', cm[0][0])
  print('Legitimate Customers Incorrectly Detected (False Positives): ',
        cm[0][1])
  print('Loan Deafulters  Missed (False Negatives): ', cm[1][0])
  print('Loan Deafulters Detected (True Positives): ', cm[1][1])
  print('Total Loan Deafulters Customers: ', np.sum(cm[1]))


def submission_nn(model,
               test_features,
               orig_test_df,
               submission_name='nn_submission_3.csv'):

  predictions = model.predict_classes(test_features)
  prediction_arr = predictions.reshape(-1,)
  prediction_df = pd.DataFrame(prediction_arr)
  prediction_df.hist()

  submission = pd.concat([orig_test_df['Col1'], prediction_df], axis=1)
  submission = submission.rename(columns={0: 'Col2'})
  submission['Col2'].value_counts()
  submission.head()
  submission.to_csv(MODEL_PATH + submission_name, index=False)

  print("Values : ", submission['Col2'].value_counts())


def submission_lgbm(model_file_path,
                    test_features,
                    orig_test_df,
                    submission_name='submission_lgb.csv'):
  lgb_forest = utils.model_read(model_file_path)
  num_lgbm_ensemble = len(lgb_forest)
  preds = np.zeros((len(test_features), 1))
  for lgbc in lgb_forest:
    preds = preds + lgbc.predict_proba(test_features)[:, 1].reshape(-1, 1)

  preds = preds / num_lgbm_ensemble

  submission_df = pd.DataFrame()
  sub_list = {'Col1': orig_test_df['Col1']}
  submission_df = pd.DataFrame(sub_list)
  submission_df['score'] = preds
  submission_df['Col2'] = 0
  submission_df.loc[submission_df['score'] > 0.28945, 'Col2'] = 1
  submission_df[['Col1', 'Col2']].to_csv(os.path.join(MODEL_PATH,
                                                      submission_name),
                                         index=False)
  print("Values : ", submission_df['Col2'].value_counts())


def submission_default(model,
                  test_features,
                  orig_test_df,
                  submission_name='nn_submission_3.csv'):

  predictions = model.predict_proba(test_features)[:,1]

  submission = pd.concat([orig_test_df['Col1'], pd.Series(predictions, name='Col2')], axis=1)
  submission.to_csv(MODEL_PATH + submission_name, index=False)
  print("Values : ", submission['Col2'].value_counts())
