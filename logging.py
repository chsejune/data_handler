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
fh = logging.FileHandler('log_filename.txt', encoding="utf-8")
fh.setLevel(logging.DEBUG)
fh.setFormatter(formatter)
logger.addHandler(fh)

# log 스트리미 출력을 위한 셋팅
sh = logging.StreamHandler()
sh.setLevel(logging.DEBUG)
sh.setFormatter(formatter)
logger.addHandler(sh)

# Debug 정보로 로그 출력 및 기록
logger.debug('This is a test log message.')

# INFO 정보로 로그 출력 및 기록 (정보 출력시 print 함수보다 이것을 사용하는 것을 권장. 로그를 남기기 위해)
logger.info("info print test")


# log 기록 파일 닫기 (파일 마지막에 선언해 주는 것을 권장함.)
fh.close()