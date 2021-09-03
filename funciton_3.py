#가변인자를 이용한 함수 호출
"""
def profile(name, age, lang1,lang2,lang3,lang4,lang5):
    print("이름 : {0}\t나이 : {1}\t".format(name,age), end=" ")
    print(lang1,lang2,lang3,lang4,lang5)

profile("유재석",20,"Python","Java","C","C++","C#")

profile("김태호",25,"Kotlin","Swift","","","")
"""
#위와 같이 하면 쓰지않는 변수들이 생기거나, 
# 또는 추가적으로 필요한 변수들이 필요할 수 있음

#가변인자 활용
def profile(name,age,*language):
    print("이름 : {0}\t나이 : {1}\t".format(name,age), end=" ")
    for lang in language:
        print(lang,end=" ")   #줄바꿈 없이 lang 모두 출력
    print() #줄바꿈 용도

profile("유재석",20,"Python","Java","C","C++","C#","JavaScript")

profile("김태호",25,"Kotlin","Swift")