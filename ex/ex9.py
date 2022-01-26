'''
지금까지 배운 내용을 복습하기 위한 퀴즈를 드리겠습니다. 직접 한 번 풀어보시고 나서 정답을 확인해주세요.

Quiz) 주어진 코드를 활용하여 부동산 프로그램을 작성하시오.

(출력 예제)
총 3대의 매물이 있습니다.
강남 아파트 매매 10억 2010년
마포 오피스텔 전세 5억 2007년
송파 빌라 월세 500/50 2000년

[코드]
class House:
    # 매물 초기화 : 위치, 건물 종류, 매물 종류, 가격, 준공년도
    def __init__(self, location, house_type, deal_type, price, completion_year):
        pass

    # 매물 정보 표시
    def show_detail(self):
        pass

이번 퀴즈는 주어진 클래스를 완성하는 것이 목표입니다. 생성자를 통해 멤버변수를 정의하고 매물 정보를 표시하기 위한 show_detail() 메소드에서는 멤버변수를 순서대로 출력합니다.

 

클래스를 완성한 뒤에는 퀴즈에 소개된 3대 매물에 대한 House 객체를 만들고 총 매물 수를 출력한 뒤 각 매물의 정보를 표시하기 위해 show_detail() 메소드를 호출합니다.
'''

class House:
    # 매물 초기화 : 위치, 건물 종류, 매물 종류, 가격, 준공년도
    def __init__(self, location, house_type, deal_type, price, completion_year):
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year
        

    # 매물 정보 표시
    def show_detail(self):
        print("{0} {1} {2} {3} {4}".format(self.location,self.house_type,self.deal_type,self.price,self.completion_year))  # 굳이 format 안써도 되네 (회고)

    
house_list = []
house_list.append(House("강남","아파트","매매","10억","2010년"))
house_list.append(House("마포","오피스텔","전세","5억","2007년"))
house_list.append(House("송파","빌라","월세","500/50","2000년"))


print("총 {}대의 매물이 있습니다.".format(len(house_list)))
for list in house_list:
    list.show_detail()
