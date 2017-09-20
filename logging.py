__author__ = 'Sejune Cheon'

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
fh.setLevel(logging.DEBUG) #위에서 logger에 전역적으로 log 기록 level를 선언 했으면 별도로 하지 않아도 됨 (수준을 다르게 가져가고 싶을때 설정하기)
fh.setFormatter(formatter)
logger.addHandler(fh)

# log 스트리미 출력을 위한 셋팅
sh = logging.StreamHandler()
sh.setLevel(logging.DEBUG) #위에서 logger에 전역적으로 log 기록 level를 선언 했으면 별도로 하지 않아도 됨 (수준을 다르게 가져가고 싶을때 설정하기)
sh.setFormatter(formatter)
logger.addHandler(sh)

# Debug 정보로 로그 출력 및 기록
logger.debug('This is a test log message.')

# INFO 정보로 로그 출력 및 기록 (정보 출력시 print 함수보다 이것을 사용하는 것을 권장. 로그를 남기기 위해)
logger.info("info print test")


# log 기록 파일 닫기 (파일 마지막에 선언해 주는 것을 권장함.)
fh.close()
#OR
# handler 들을 logger라는 변수에 담아서 다닐 경우 아래 처럼 기록 파일 닫기를 수행한다.
logger.handlers[1].close()
logger.removeHandler(logger.handlers[1])
