import click
import yaml
import time
import sys
import os
from loguru import logger
from yaml.loader import SafeLoader

def read_yaml(path, yaml_file, value):
    full_path = os.path.join(path, f'{yaml_file}.yml')
    if os.path.exists(full_path):
        logger.debug(f"arquivo existe {full_path}")
        with open(full_path, 'r') as config:
            data = yaml.load(config, Loader=SafeLoader)
        return data[value]
    else:
        logger.warning(f"Arquivo não encontrado: {full_path}")