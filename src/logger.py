import logging
import time

from pathlib import Path

try:
    log_dir = Path(__file__).parent/'logs'
    log_dir.mkdir(parents= True, exist_ok= True)
except Exception as e:
    logging.error(str(e))

timestr = time.strftime('%d%m%Y-%H%M%S')
log_filename = 'log_'+timestr+'.log'
log_filepath = log_dir.joinpath(log_filename)

log_format = '%(asctime)s=>%(levelname)-8s:%(filename)-25s:%(funcName)-25s:%(lineno)-4s%(message)s'

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler(log_filepath)
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(logging.Formatter(log_format))

logger.addHandler(file_handler)
