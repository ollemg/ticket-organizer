import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from loguru import logger
from .config import config
import click

def send_mail(date, message):
    logger.debug("Iniciando função send")
    try:
        mail_body = f"Atividades {date}"
        mail_subject = f"Atividades {date}"
        mimemsg = MIMEMultipart()
        mimemsg['From']=config('sender')
        mimemsg['To']=config('receivers')
        mimemsg['Subject']=mail_subject
        mimemsg.attach(MIMEText(message, 'plain'))
        connection = smtplib.SMTP(host=config('smtp_server'), port=config('port'))
        connection.starttls()
        connection.login(config('sender'),config('password'))
        connection.send_message(mimemsg)
        connection.quit()
        logger.info(f"Email enviado. from: {config('sender')}, to: {config('receivers')}, subject: {mail_subject}, message: {message}")
    except (smtplib.SMTPAuthenticationError) as error:
        logger.error(error)
    logger.debug("Saindo função send")