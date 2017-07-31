__author__ = 'Sejune Cheon'

# 개발환경: python3

# pandas library 불러오기
import pandas as pd


# csv 파일 데이터 읽어드리기
df = pd.read_csv('datasets/raw_data.csv')


# 불러들인 데이터 테이블에 대한 컬럼명 조회
print(df.columns.values) # 그냥 "df.columns" 하면 모든 컬럼명을 보여주지 못함


# 컬럼 명이 특정 조건에 맞는 경우만 추출하기
sub_df = df.filter(regex=r'I[0-9]') # regular expression 이용, # 열 목록 중에 'I' 로 시작하고 뒤에 숫자가 오는 열 이름을 가진 데이터들 모두 추출
sub_df = df['Y'] # 'Y' 라는 이름을 가진 열 데이터 추출


# 각각의 데이터 조건이 맞는 경우 추출하기
sub_df = df[df['Y']==0] # df['Y'] 열의 값들 중 값이 '0' 인 경우의 df 데이터들 추출하기 (df와 sub_df의 열 개수는 같음)


# 각 열 별로 'NaN' 개수 카운트
sub_df.isnull().sum()



