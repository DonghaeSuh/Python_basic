students = range(1,6)
print(students)
students= [i+100 for i in students]  #students 에서 i번째를 값를 하나씩 꺼내와서 i+100한 값을 list형태로 student에 집어넣어라
print(students)

#학생 이름을 길이로 변환
students =["Iron man","Thor","Mynameis"]
students = [len(i) for i in students]
print(students)

#학생 이름을 대문자로 변환
students =["Iron man","Thor","Mynameis"]
students = [i.upper() for i in students]
print(students)