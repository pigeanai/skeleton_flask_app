import logging
import logging.handlers
import os
from flask import Flask

from config import Config

def set_up_logging(app: Flask):
    if not os.path.exists('logs'):
        os.mkdir('logs')
    if app.logger.hasHandlers():
        app.logger.handlers.clear()

    logging_formatter = logging.Formatter('%(asctime)s %(levelname)s: %(message)s ')
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(logging_formatter)
    app.logger.addHandler(stream_handler)
    rotating_file_handler = logging.handlers.RotatingFileHandler(
        'logs/flaskapp.log',
        maxBytes=10240, 
        backupCount=10
    )
    rotating_file_handler.setFormatter(logging_formatter)
    app.logger.addHandler(rotating_file_handler)
    app.logger.setLevel(Config.LOG_LEVEL)