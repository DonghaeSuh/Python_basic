"""
random 모듈의 shuffle과 sample 연습

20명중 
1명의 치킨 당첨자
3명의 커피 당첨자 추첨


"""


#타입 1

from random import *

"""
lst = range(1,21)   #1부터 21 전까지 생성
lst = list(lst)   #리스트 타입으로 전환

shuffle(lst)  #순서 섞음
winners = sample(lst,4)

print("-- 당첨자 발표 --")
print("치킨 당첨자 : {0}".format(winners[0]))
print("커피 당첨자 : {0}".format(winners[1:]))
print("-- 축하합니다 --")

"""


#타입 2
"""
users = range(1,21)
users = list(users)

one = sample(users,1)

users.pop(one[0]-1)

three = sample(users,3)

print("-- 당첨자 발표 --")
print("치킨 당첨자 : {0}".format(one[0]))
print("커피 당첨자 : {0}".format(three))
print("-- 축하합니다 --")


"""