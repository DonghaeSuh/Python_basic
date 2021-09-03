#표준 체중 (각 개인의 키에 적당한 체중)구하는 프로그램

#표준체중 공식
#남자 : 키(m) x 키(m) x 22
#여자 : 키(m) x 키(m) x 21

#조건
#1. 표준 체중은 별도의 함수 내에서 계산
#     *함수명 :std_weigt
#     *전달값 :키(height),성별(gender)
#2. 표준 체중은 소수점 둘째자리까지 표시

#출력예제   = > 키 175cm의 남자의 표준 체중은 67.38kg 이다.

height = int(input("키 몇cm? "))
gender = input("[성별 남자 or 여자 입력]")
std = 0

def std_weight(height,gender):
    if gender =="남자": #남자
        return (height/100)**2*22
    else:
        return (height/100)**2*21

std = round(std_weight(height,gender),2)

print("키 {0}cm의 {1}의 표준 체중은 {2}kg 이다.".format(height,gender,std))