import click
import yaml
import time
import sys
import os
from loguru import logger

def create_yaml(path, yaml_file, content):
    logger.debug(f"Entrando na função create_yaml")
    full_path = os.path.join(path, f'{yaml_file}.yml')
    if os.path.exists(full_path):
        logger.warning(f"Arquivo existe {full_path}")
    else:
        with open(full_path, 'w') as yaml_file:
            yaml.dump(content, yaml_file, default_flow_style=False)
            logger.info(f"Arquivo criado {full_path}")
    logger.debug(f"Saindo na função create_yaml")