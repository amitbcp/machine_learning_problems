from localconfig import LocalConfig
from configparser import ExtendedInterpolation, ConfigParser, SafeConfigParser
import configparser
import sys
import os
import collections


class CGNConfigParser():
  """This class is used to parse the config file

  Attributes:
      central_config (str): Description
      config_dict (dict): Description
      env_configs (dict): Description
      path_to_config_ini (str): Description
  """

  def __init__(self,
               path_to_config_ini=None,
               env_configs_check=False,
               logger=None):
    """Summary

    Args:
        path_to_config_ini (None, optional): Description
        env_configs_check (bool, optional): Description
    """
    #print (path_to_config_ini)
    # self.logger = logger
    # or abzlogger()
    CGN_DS_ROOT = \
      os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                   '..', '..')
    self.path_to_config_ini = path_to_config_ini or \
      os.path.join(CGN_DS_ROOT, 'common',
                   'config_files', 'config.ini')
    self.config_dict = {}
    self.central_config = None

    # Parse central config first
    central_config_file = os.path.join(CGN_DS_ROOT, 'common', 'config_files',
                                       'config.ini')
    self.parse_config(central_config_file)

    # Parse user specified now if provided
    if self.path_to_config_ini != \
        central_config_file and self.path_to_config_ini != None :
      self.parse_config(self.path_to_config_ini)

    # checks whether config_dict should be updated with os environ values,
    # if True (1) retrieves all the os environs who has prefix "dsenv_"
    # (2) creates os environ dict (3) updates main config_dict
    if env_configs_check:
      self.env_configs = {}
      for k, v in dict(os.environ).items():
        if k.startswith('dsenv_'):
          k = k[6:]
          config_list = k.split("__")
          self.build_env_dict(self.env_configs, config_list, v)
      self.update_dict(self.config_dict, self.env_configs)

  def printall(self, out_file=None):
    """Summary

    Args:
        out_file (None, optional): Description
    """
    if out_file is not None:
      if os.path.exists(out_file):
        self.central_config.save(out_file)
      else:
        print("Couldn't find out_file '{}'...".format(out_file))
    else:
      import yaml
      print(yaml.dump(self.config_dict, default_flow_style=False))

  def parse_config(self, config_file):
    """Summary

    Args:
        config_file (str): Description
    """
    # check if config file exists
    if not os.path.exists(config_file):
      print("Couldn't find config_file '{}'...".format(config_file))
      sys.exit(-1)
    try:
      self.central_config = LocalConfig(config_file, interpolation=True)
    except Exception as e:
      print(e)
      print("Issue with LocalConfig")
      sys.exit(-21)

    try:
      self.central_config._parser = \
        ConfigParser(interpolation=ExtendedInterpolation())
    except Exception as e:
      print(e)
      print("Issue with ConfigParser")
      sys.exit(-22)

    sections = list(self.central_config)
    #Prepare config_dict
    source_dict = {}
    for section in sections:
      # TODO add exception handling configparser.InterpolationMissingOptionError
      source_dict[section] = dict(self.central_config.items(section))

    self.update_dict(self.config_dict, source_dict)

    # Configure sections
    for section in sections:
      if '.' in section:
        self.config_dict[section.split('.')[0]]\
          [section.split('.')[1]] = self.config_dict[section]
        self.config_dict.pop(section, None)

  def update_dict(self, target_dict, source_dict):
    """Summary

    Args:
        target_dict (str): Description
        source_dict (str): Description
    """
    for k, v in source_dict.items():
      if (k in target_dict and isinstance(target_dict[k], dict) \
          and isinstance(source_dict[k], collections.Mapping)):
        self.update_dict(target_dict[k], source_dict[k])
      else:
        target_dict[k] = source_dict[k]

  def build_env_dict(self, env_configs, config_list, env_val):
    """updates os environ dict env_configs

    Args:
        env_configs (dict): os environment dictionary
        config_list (list): contains hierarchy of config in flat form. For ex:
          if os env is dsenv_service_coordinator__sharding_policy__fixed_shard_count
          this list will contain ["service_coordinator",
          "sharding_policy", "fixed_shard_count"]
        env_val (str/int): os environ value
    """
    head = config_list[0]
    tail = config_list[1:]
    if not tail:
      env_configs[head] = env_val
    else:
      if head not in env_configs:
        env_configs[head] = {}
      self.build_env_dict(env_configs[head], config_list[1:], env_val)

  def get_sub_config(self, type_of_config):
    """Summary

    Args:
        type_of_config (str): Description

    Returns:
        str: Description
    """
    if type_of_config == 'all':
      return self.config_dict
    return self.config_dict[type_of_config]

  def get_sub_config_section(self, section):
    """Summary

    Args:
        section (str): Description

    Returns:
        str: Description

    Raises:
        Exception: Description
    """
    #Currently only allow section depth = 2
    try:
      sub_config_name, section_name = section.split('.')
    except:
      raise Exception('input section error')
    sub_config = self.config_dict[sub_config_name]
    section_config = sub_config[section_name]
    #sub section should inherit all configurations from its parent
    for k, v in sub_config.items():
      if (not isinstance(v, dict)) and (k not in section_config):
        section_config[k] = v
    return section_config

  def is_file(self, filename):
    """Summary

    Args:
        filename (str): Description

    Returns:
        str: Description
    """
    if 'checkpoint-299000' in filename:
      return True
    basename = os.path.basename(filename)
    if len(basename.split('.')) > 1:
      return True
    return False

  def sanity_check(self):
    """Sanity check
    """
    check_file_permission = self.check_file_permission(self.config_dict)
    if check_file_permission == False:
      print(
        "\n******* Config file sanity check failed. Please review '{}'".format(
          self.path_to_config_ini))
      sys.exit(-1)

  def __getitem__(self, section):
    return self.config_dict.__getitem__(section)


if __name__ == "__main__":
  config = CGNConfigParser()
  config.printall()
  print(config.get_sub_config('automation'))
  # print (config.config_dict)
  config.sanity_check()
