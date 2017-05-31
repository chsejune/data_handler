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

# log 파일 기록을 위한 셋팅
fh = logging.FileHandler('log_filename.txt')
fh.setLevel(logging.DEBUG)
fh.setFormatter(formatter)
logger.addHandler(fh)

# log 스트리미 출력을 위한 셋팅
sh = logging.StreamHandler()
sh.setLevel(logging.DEBUG)
sh.setFormatter(formatter)
logger.addHandler(sh)
logger.debug('This is a test log message.')