#50명의 승객과 매칭 기회가 있을 때, 총 탑승 승객수
#조건 
# 1. 승객별 운행 소요 시간은 5~50 분 사이의 난수로 정해짐
# 2. 당신은 소요 시간 5~15분 사이의 승객만 매칭해야 한다.


#출력문 예제
#[0] 1번쨰 손님 (소요시간 :15분)
#[ ] 2번째 손님 (소요시간 :50분)
#[0] 3번째 손님 (소요시간 :5분)
#....

#총 탑승 승객 : 2 명

from random import *


accounts = range(1,51)
num = 1
choosen_num = 0

accounts = [randrange(1,51) for i in accounts]

for i in accounts:
    if accounts[num-1]>15:
        print("[ ] {0}번째 손님 (소요시간 :{1}분)".format(num,accounts[num-1]))
        num+=1
        continue
    print("[0] {0}번째 손님 (소요시간 :{1}분)".format(num,accounts[num-1]))
    num+=1
    choosen_num +=1
print("총 탑승 승객 : {0} 명".format(choosen_num))


#하지만 이것은 비 효율적 또한 5분 이상 까먹고 않넣음
"""
미리 만들어서 다 넣는 것 보다
그때 그때 만들어서(현실과 유사)
그에 해당하는 값 출력하고 다음 차례 반복문으로 넘어가는 것이 코드 절약
"""

"""
from random import *
cnt = 0  # 총 탑승 승객 수

for i in range(1,51):          # 각 승객
    time = randrange(1,51)   #소요시간
    if 5<= time <= 15:   #태울 손님 
        print("[0] {0}번째 손님 (소요시간 :{1}분)".format(i,time))
        cnt +=1
    else:     #안 태울 손님
        print("[ ] {0}번째 손님 (소요시간 :{1}분)",format(i,time))
print("총 탑승 승객 : {0} 분".format(cnt))        

"""