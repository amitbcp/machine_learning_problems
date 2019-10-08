import os
import pickle
import time

from common.config_files.config import CGNConfigParser

config_all = CGNConfigParser()
config_general = config_all.get_sub_config('general')
config = config_all.get_sub_config('general')
model_path = config_general['hackathon']


def model_save(model):
  """
  Dumps model into pickle file

  Args:
		model: Model to be saved

	Returns:
		Filepath of the model file

	Raises:
		Exception: File not found exception
  """
  model_file_path = os.path.join(
    model_path,
    time.strftime("run_%Y_%m_%d-%H_%M_%S") + ".pickle")
  pickle.dump(model, open(model_file_path, 'wb'))
  return model_file_path


def model_read(model_file_path):
  """
    Reads the model and return the object

    Args:
  		model_file_path: Model file path to be read

  	Returns:
  		model object

  	Raises:
  		Exception: File not found exception
    """
  with open(model_file_path, 'rb') as f:
    model = pickle.load(f)

  return model