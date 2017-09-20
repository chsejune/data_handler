__author__ = 'Sejune Cheon'

# 개발환경: python3

# pandas library 불러오기
import pandas as pd


# csv 파일 데이터 읽어드리기
df = pd.read_csv('datasets/raw_data.csv')

# 데이터 프레임의 상위 x개 만큼만 불러오기 (default=5)
df.head(10) # 상위 10개의 행 데이터 불러오기
df.tail(10) # 하위 10개의 행 데이터 불러오기


# 불러들인 데이터 테이블에 대한 컬럼명 조회
print(df.columns.values) # 그냥 "df.columns" 하면 모든 컬럼명을 보여주지 못함


# 특정 조건에 해당하는 컬럼명만 뽑기
df.columns.values[df.isnull().sum()==0] # null 셀이 없는 열들 뽑기


# 컬럼 명이 특정 조건에 맞는 경우만 추출하기
sub_df = df.filter(regex=r'I[0-9]') # regular expression 이용, # 열 목록 중에 'I' 로 시작하고 뒤에 숫자가 오는 열 이름을 가진 데이터들 모두 추출
sub_df = df['Y'] # 'Y' 라는 이름을 가진 열 데이터 추출


# 명시된 컬럼 지우기
df.drop(['A', 'B'], axis=1, inplace=True) # 'A' 컬럼과 'B' 컬럼 지우기, axis=1 지정을 통해 해당 컬럼 지우기, axis=0 일 경우 해당 row 가 지워짐, inplace=True 지정을 통해 sub_df=sub_df.drop(['A', 'B'], axis=1) 이렇게 안해도 됨(re-assign option).


# 명시된 행 지우기
df.drop([0,1], axis=0, inplace=True) # 행번호 0과 1 지우기, axis=0 으로 설정 시 행 기준으로 지우기가 실행됨


# 데이터 프레임 indexing 다시 하기
df.reset_index(drop=True, inplace=True) # 행 index reset, drop=True 로 해야 기존 index를 보존하지 않음, drop=False 설정 시 기존 행 index를 보존


# 각각의 데이터 조건이 맞는 경우 추출하기
sub_df = df[df['Y']==0] # df['Y'] 열의 값들 중 값이 '0' 인 경우의 df 데이터들 추출하기 (df와 sub_df의 열 개수는 같음)


# 각 열 별로 'NaN' 개수 카운트
df.isnull().sum()


# 새로운 항목(열) 만들기
## Y 변수(class label) 숫자로 변환
# P=0, F=1
df['Y_num'] = pd.Categorical(df['Y'], ['P', 'F']).codes


