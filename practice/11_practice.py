# 모듈
"""
import theater_module # theater_module 을 가져다가 사용
theater_module.price(3) # 3명이 영화 보러 갔을 때 가격
theater_module.price_morning(4) # 4명이 조조 영화 보러 갔을 때
theater_module.price_soldier(5) # 5명이 군인이 영화 보러 갔을 때

import theater_module as mv # theater_module 을 새로운 별명인 mv 로 사용
mv.price(3)
mv.price_morning(4)
mv.price_soldier(5)

from theater_module import * # theater_module 내에서 모든 것을 가져다가 사용
price(3) # theater_module. 필요 없음
price_morning(4)
price_soldier(5)

from theater_module import price_soldier as price # price_soldier 를 새로운 별명인 price 로 사용
price(5) # price_soldier() 를 호출

"""

# 패키지

"""
import travel.thailand #import 는 패키지와 모듈까지만 사용 가능
trip_to = travel.thailand.ThailandPackage()
trip_to.detail()

import travel.thailand.ThailandPackage # 클래스 직접 import 불가 => 에러

from travel.thailand import ThailandPackage # travel.thailand 모듈에서 ThailandPackage 클래스 가져오기
trip_to = ThailandPackage() # travel.thailand. 는 생략
trip_to.detail()

"""

# __all__


#__init__.py 수정

"""
from travel import *
# trip_to = vietnam.VietnamPackage()
trip_to = thailand.ThailandPackage() # 태국
trip_to.detail()
"""

# 모듈 직접 실행
"""
from travel import *
trip_to = thailand.ThailandPackage()
trip_to.detail()
"""

# 패키지, 모듈 위치

"""
import inspect
import random
print(inspect.getfile(random)) # random 모듈의 위치

import inspect
from travel import *
print(inspect.getfile(thailand)) # thailand 모듈의 위치
"""

# 내장함수
# dir : directory


"""
print(dir())
import random # random 모듈 가져다 쓰기
print(dir())
import pickle # pickle 모듈 가져다 쓰기
print(dir())

import random
print(dir(random))

lst = [1, 2, 3]
print(dir(lst))

name = "Jim"
print(dir(name))
"""

# 외장함수

"""
import glob
print(glob.glob("*.py")) # 확장자가 py 인 모든 파일
"""


"""
import os

folder = "sample_dir"

if os.path.exists(folder): # 폴더가 존재한다면
    print("이미 존재하는 폴더입니다.")
else: # 폴더가 존재하지 않으면
    os.makedirs(folder) # 폴더 생성
    print(folder, "폴더를 생성하였습니다.")
"""



"""
import os

folder = "sample_dir"

if os.path.exists(folder):
    print("이미 존재하는 폴더입니다.")
    os.rmdir(folder) # 폴더 삭제
    print(folder, "폴더를 삭제하였습니다.") # 삭제 문구 출력
else:
    os.makedirs(folder)
    print(folder, "폴더를 생성하였습니다.")

"""

"""
import os
print(os.listdir())
"""

"""
import time
print(time.localtime())

import time
print(time.strftime("%Y-%m-%d %H:%M:%S")) # 연-월-일 시:분:초
"""
"""
import datetime
today = datetime.date.today() # 오늘 날짜 저장
td = datetime.timedelta(days=100) # 100일 저장
print(td)
print(today)
print("우리가 만난지 100일은", today + td) # 오늘부터 100일 후
"""