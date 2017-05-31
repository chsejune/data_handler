## how to log when running program

## tested in python3

# import library
import logging

# log file 기록 및 출력을 위한 셋팅
logger = logging.getLogger()

# log 기록 level
logger.setLevel(logging.DEBUG) # INFO, DEBUG, WARNING, ERROR

# log 기록 포멧
# formatter = logging.Formatter('%(asctime)s %(levelname)s: %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
# formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
formatter = logging.Formatter('%(message)s')

# log 
fh = logging.FileHandler('log_filename.txt')
fh.setLevel(logging.DEBUG)
fh.setFormatter(formatter)
logger.addHandler(fh)

ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
ch.setFormatter(formatter)
logger.addHandler(ch)
logger.debug('This is a test log message.')