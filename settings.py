import os
import logging
import configparser

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Logging
pylogger = logging.getLogger(__name__)
pylogger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
postgresql_folder = os.path.join(BASE_DIR, "PostgreSQL")

# Config
config = configparser.ConfigParser()
config.read('config.ini')