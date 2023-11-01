# import 할때
# 패키지.파일 부분에 파일만 들어올 수 있다.
# 클래스를 호출하고 싶다면 from ~ import문 사용
# import travel.thailand
# trip_to = travel.thailand.ThailandPackage()
# trip_to.detail()

# from travel.thailand import ThailandPackage 
# trip_to = ThailandPackage()
# trip_to.detail()

# from travel import vietnam
# trip_to = vietnam.VietnamPackage()
# trip_to.detail()

# __all__
#패키지 생성 및 사용
from travel import *
# # trip_to = vietnam.VietnamPackage()
# trip_to = thailand.ThailandPackage()
# trip_to.detail()

# 패키지, 모듈 위치
import inspect # 파일의 경로를 출력해주는 메서드를 가진 모듈
import random
print(inspect.getfile(random)) # C:\pythonStudy\pythonStudy\travel\thailand.py
print(inspect.getfile(thailand))

# pip install
# pip로 패키지 설치방법

# from bs4 import BeautifulSoup
# soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
# print(soup.prettify())

# 내장 함수
# input : 사용자 입력을 받는 함수
# language = input("무슨 언어를 좋아하세요?")
# print(f"{language}은 아주 좋은 언어입니다!.")

# dir : 어떤 객체를 넘겨줬을 때 그 객체가 어떤 변수와 함수를 가지고 있는지 표시
# print(dir())
# import random # 외장 함수
# print(dir)
# import pickle
# print(dir(random))

# lst = [1, 2, 3]
# print(dir(lst))

# name = "Jim"
# print(dir(name))

# 외장함수
# 내장함수와 다르게 직점 import해서 사용해야함
# glob : 경로 내의 폴더 / 파일 목록 조회(윈도우 dir)
import glob
print(glob.glob("*.py")) # 확장자가 py인 모든 파일

# os : 운영체제에서 제공하는 기본 기능
import os
print(os.getcwd()) # 현재 디렉토리

# folder = "sample_dir"

# if os.path.exists(folder) :
#     print("이미 존재하는 폴더 입니다.")
#     os.rmdir(folder)
#     print(folder, "폴더를 삭제 하였습니다.")
# else :
#     os.makedirs(folder) # 폴더 생성
#     print(folder, "폴더를 생성하였습니다.") 
print(os.listdir())

# time : 시간 관련 함수
import time
print(time.localtime())
print(time.strftime("%Y-%m-%d %H:%M:%S"))

import datetime
print("오늘 날짜는", datetime.date.today())
today = datetime.date.today() # 오늘 날짜 저장
td = datetime.timedelta(days=100) # 100일 저장
print("우리가 만난지 100일은", today + td)

# 실습
#프로젝트 내에 나만의 시그니처를 남기는 모듈을 만드시오
# 조건 : 모듈 파일명은 byme.py 로 작성#
import module
module.sign()