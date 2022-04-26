import click
import yaml
from yaml.loader import SafeLoader
from loguru import logger


def config(param):
    try:
        with open('./config.yml', 'r') as config:
            data = yaml.load(config, Loader=SafeLoader)
            return data[param]
    except (KeyError, NameError) as error:
        return logger.error(f'chave {error} não foi encontrada no arquivo ./config.yml: ')
