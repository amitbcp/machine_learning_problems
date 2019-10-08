from sklearn import metrics
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from common.config_files.config import CGNConfigParser

config_all = CGNConfigParser()
config = config_all.get_sub_config('hdfc')
model_path = config['model_path']


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


def submission(model,
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
  submission.to_csv(model_path + submission_name, index=False)

  print("Values : ", submission['Col2'].value_counts())