#지역변수와 전역변수

"""
gun =10

def checkpoint(soldiers):  #경계근무
    global gun  #전역 공간에 있는 gun 사용
    gun = gun-soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))

print("전체 총: {0}".format(gun))
checkpoint(2) #2명 경계근무
print("남은 총 : {0}".format(gun))
"""

gun =10

def checkpoint_ret(soldiers,gun):  #경계근무
      #전역 공간에 있는 gun 사용
    gun = gun-soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))
    return gun

print("전체 총: {0}".format(gun))
gun = checkpoint_ret(2,gun) #2명 경계근무, gun 변화한 것 return 을 통해 전체 gun 의 변화를 준다
print("남은 총 : {0}".format(gun))