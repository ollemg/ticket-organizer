#!/usr/bin/env python
import glob
import os
import sys
import time
from datetime import date, timedelta
from os.path import expanduser
import click
import yaml
from yaml.loader import SafeLoader
from .config import config
from loguru import logger
from .create_yaml import create_yaml
from .read_yaml import read_yaml
from .mail import send_mail
# from .logger
logger.remove()

format_logger="<green>{time}</green> | <level>{level}</level> | <blue>{name}:{function}:{line}</blue> - <level>{message}</level>"
format_stderr="<level>{level}</level> - <level>{message}</level>"

logger.add(
    sys.stdout,
    level="DEBUG",
    colorize=True,
    format=format_stderr,
)

logger.add(
    "ticket-organizer.log", 
    # rotation="10 KB",
    level="DEBUG",
    format=format_logger,
)

trace = '-----------------------------------'
greetings = """Boa tarde,
Segue chamados atendidos no dia de hoje:
"""

title = f"""{trace}
Resumo das atividades diarias:
{trace}
"""
working_hours = f"""
{trace}
Horas Trabalhadas:
{trace}
"""
att = '\natt,'
pwd = os.getcwd()
today = date.today()
days_ago = today - timedelta(days=1)


@click.group('cli')
def cli():
    logger.debug("Iniciando cli")
    ...


@cli.command('create', help='Cria o yaml')
@click.argument('path', type=click.Path(exists=True), default=config('activities'))
def create(path):
    logger.debug("Iniciando função create")
    logger.debug(f'path: {path}')
    """Cria um yml baseado na data atual"""
    dicts = {
        'meeting': [
            {
                'name': 'Reuniao equipe Linux',
                'schedule': '08:15 - 08:30',
                'register': False,
            },
        ],
        'tickets': [
            {'name': '', 'type': '', 'schedule': '', 'register': False},
        ],
    }
    create_yaml(path, today, dicts)

@cli.command('resume', help='Lê o yaml')
@click.argument('path', type=click.Path(exists=True, readable=True), default=config('activities'))
@click.option('-r', 'register', is_flag=True)
def resume(path, register):
    logger.debug("Iniciando função read")
    logger.debug(f'path: {path}, register: {register}')
    """Lê o yaml"""
    list_hours = []
    list_tickets = []
    tickets_yml = read_yaml(path, today, 'tickets')
    meeting_yml = read_yaml(path, today, 'meeting')

    click.secho(title, fg='green', bold=True)
    click.secho(greetings, fg='green')
    
    for i in tickets_yml:
        click.secho(i['name'], fg='green')
        list_tickets.append(i['name'])

    click.secho(att, fg='green')
    click.secho(working_hours, fg='green', bold=True)

    for i in meeting_yml:
        if i['schedule'] is list:
            for hours in i['schedule']:
                list_hours.append(hours)
        else:
            list_hours.append(i['schedule'])

    for i in tickets_yml:
        if type(i['schedule']) is list:
            for hours in i['schedule']:
                list_hours.append(hours)
        else:
            list_hours.append(i['schedule'])
    for hours in sorted(list_hours):
        click.secho(hours, fg='green')

    logger.debug("Saindo função read")
    message = f"""
    {*list_tickets,}
"""

    click.echo(message)
@cli.command('send', help='Envia o email')
@click.argument('path', type=click.Path(exists=True, readable=True), default=config('activities'))
@click.option('-y', 'yes', is_flag=True)
def send(path, yes):
    logger.debug('Entrando na função send')
    logger.debug(f'path: {path}, yes: {yes}')
    if yes:
        logger.info('Enviando e-mail')
        send_mail(today, 'teste')
    else:
        logger.info('Email não foi enviado')
    logger.debug('Saindo da função send')
@cli.command('new', help='Cria um novo ticket')
@click.argument('path', type=click.Path(exists=True, readable=True), default=config('tickets'))
@click.option('-n', '--name', type=str)
def read(path, name):
    logger.debug("Iniciando função new")
    """Cria um modelo de ticket"""
    ticket_model = {
        'registros': [
            {
            'dia': f'{today}', 
            'turno': 'tarde', 
            'tempo': 
            {
                'inicio': '08:00', 
                'fim': '09:00'
            }, 
            'atividades': 'atividades...'
        }
        ]
    }
    create_yaml(path, name, ticket_model)
    # read_yaml(path, name, 'registros')