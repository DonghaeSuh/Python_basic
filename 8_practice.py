

# sep=" "
# print("Python","Java","JavaScript",sep=" ")

# end=" "
#print("Python","Java",sep=",",end="?")
#print("무엇?")

# 로그출력 관리

# import sys
# print("Python","Java",file=sys.stdout)  #표준 출력
# print("Python","Java",file=sys.stderr)  #표준 에러


#끝에 정렬
# ljust(), rjust() 

# 시험성적
# scores = {"수학":0, "영어": 50, "코딩": 100}
# for subject,score in scores.items():
#     #print(subject,score)
#     print(subject.ljust(8),str(score).rjust(4), sep=":") 
#     #l,r 왼 우 정렬, (숫자) : 숫자만큼의 공간 
    

# # 은행 대기순번표
# #001 , 002 , 003 ...
# for num in range(1,21):
#     print("대기번호 : "+str(num).zfill(3))


# #표준 입력
# answer = input("아무 값이나 입력: ")  # 문자열 형태(str) answer에 저장됨
# print("입력하신 값은 " + answer + "입니다.")
# print(type(answer))

#다양한 출력 포멧--------------------------------------------------
#빈 자리는 빈공간으로 두고, 오른쪽 정렬, 총 10자리 공간 확보 <=> {0: >10}
#print("{0: >10}".format(500))

#양수일 땐 + 로 표시, 음수일 땐 -로 표시 (+를 안적으면 양수일때는 그대로, 음수일 때는 -붙음)
# print("{0: >+10}".format(500))
# print("{0: >+10}".format(-500))

# 왼쪽 정렬, 빈칸을 _로 채움
# print("{0:_<10}".format(500))

# # 3자리마다 콤마
# print("{0:,}".format(100000000000)) # 3자리 마다 콤마 찍어주기
# print("{0:+,}".format(100000000000)) # + 기호, 3자리 마다 콤마 찍어주기

# 복잡한 조합
# # 빈 자리는 ^ 로, 좌측 정렬, + 기호, 30 칸의 공간 확보, 3자리 마다 콤마 찍어주기
# print("{0:^<+30,}".format(100000000000))

# 소숫점 출력
# print("{0:f}".format(5/3)) # 실수 값 출력 / 소숫점 6번째 자리 까지 (기본)
# print("{0:.2f}".format(5/3)) # 실수 값 출력 / 소숫점 2번째 자리 까지 (설정)

# 총정리
# print 내에서 
# {인덱스:[[빈자리채우기]정렬][기호][확보공간][콤마][.자릿수][타입]}

#파일 입출력----------------------------------------------------------------

# score_file = open("score.txt", "w", encoding="utf8") # score.txt 파일을 쓰기("w") 모드로 열기
# print("수학 : 0", file=score_file) # score.txt 파일에 내용 쓰기
# print("영어 : 50", file=score_file) # score.txt 파일에 내용 쓰기
# score_file.close() # score.txt 파일 닫기

# score_file = open("score.txt", "a", encoding="utf8") # score.txt 파일을 쓰기("a") 모드로 열기
# score_file.write("과학 : 80") # print("과학 : 80", file=score_file,end="") 도 가능
# score_file.write("\n코딩 : 100") # write 는 줄바꿈 안해주기 때문에 탈출문자(\n)로 줄바꿈 추가
# score_file.close()

#read() 함수는 파일의 전체 내용을 한 번에 읽어오기
# score_file = open("score.txt", "r", encoding="utf8") # score.txt 파일을 읽기("r") 모드로 열기
# print(score_file.read()) # 파일 전체 읽어오기
# score_file.close()

#readline() 함수를 이용하면 한 줄 단위로 불러오기
# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.readline(), end="") # 줄별로 읽기. 한 줄 읽고 커서는 다음 줄로 이동
# print(score_file.readline(), end="") # 줄바꿈 중복을 방지하기 위해 end="" 처리
# print(score_file.readline(), end="")
# print(score_file.readline(), end="")
# score_file.close()

#각 문장마다 end="" 를 통해 줄바꿈을 하지 않도록 처리
# 이유:  현재 파일에 쓰여진 각 문장은 끝에 줄바꿈을 포함하고 있기 때문에 
#        print() 자체의 줄바꿈과 중복으로 실행되는 증상을 막기 위해서

#while문으로 더이상 읽으려는 줄이 없을 때 반복문 탈출

# score_file = open("score.txt", "r", encoding="utf8")

# while True:
#     line = score_file.readline()
#     if not line: # 더 이상 읽어올 내용이 없으면?
#         break # 반복문 탈출
#     print(line, end="") # 읽어온 줄 출력. 줄바꿈 중복을 방지하기 위해 end="" 처리
    
# score_file.close()

# # 파일 내용을 한 번에 불러와서 리스트에 저장해두고 리스트를 반복 순회하면서 내용을 출력
# score_file = open("score.txt", "r", encoding="utf8")

# lines = score_file.readlines() # 모든 줄을 읽어와서 list 형태로 저장
# # print(lines) => ['수학 : 0\n', '영어 : 50\n', '과학 : 80\n', '코딩 : 100'] 처럼 저장됨 
# #  \n 이 나오면 다음 차례로 넘어간다.
# for line in lines:
#     print(line, end="") # 읽어온 줄 출력. 줄바꿈 중복을 방지하기 위해 end="" 처리
# score_file.close()

#pickle-----------------------------------------------------------
# import pickle # pickle 모듈 가져다 쓰기

# profile_file = open("profile.pickle", "wb") # 바이너리(binary) 형태로 저장
# profile = {"이름":"박명수", "나이":30, "취미":["축구", "골프", "코딩"]}
# print(profile)
# pickle.dump(profile, profile_file) # profile 데이터를 file 에 저장
# profile_file.close()


# profile_file = open("profile.pickle", "rb") # 읽을 때에도 바이너리(binary) 명시
# profile = pickle.load(profile_file) # file 에 있는 정보를 불러와서 profile 에 저장

# print(profile)
# profile_file.close()

# wiht -------------------------------------------------------------
# import pickle

# with open("profile.pickle", "rb") as profile_file:
#     print(pickle.load(profile_file))

# with open("study.txt", "w", encoding="utf8") as study_file:
#     study_file.write("파이썬을 열심히 공부하고 있어요")

# with open("study.txt", "r", encoding="utf-8") as study_file:
#     print(study_file.read())

