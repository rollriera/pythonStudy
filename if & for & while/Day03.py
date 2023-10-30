# if 조건문
# if 조건식 : True 일때의 실행 로직
if ("홍길동" == "홍길동") : print("실행됨")

weather = input("오늘 날씨는 어때요? ")
if weather == "비" or weather == "눈": print("우산챙기세요.") # 초기 조건
elif weather == "미세먼지" : print("마스크를 챙기세요") #else if 2번째 조건
else: print("준비물이 필요없어요") #위조건들이 전부 False일때 실행되는 조건

temp = int(input("기온은 어때요?"))
if temp == 30 : print("너무 더워요 나가지 마세요")
elif 10 <=  temp < 30 : print("괜찮은 날씨에요") # and 문을 작성하지 않아도 비교 가능
elif 0 <= temp  < 10 : print("외투를 챙기세요")
else : print("너무 추워요. 나가지 마세요")

# for문
# for 변수 in 반복할 값 : 반복 수행할 로직
for i in range(5) :
    if i != 1 : print(f"대기번호 : {i}")

# while 문
i = "홍길동"
person = "Unknown"
while person != i :
    print(f"{i}님, 커피가 준비 되었습니다.")
    person = input("이름이 어떻게 되세요? ")

# continew break
absent = [2, 5] # 출석 번호 2번 5번 결석
no_book = [7] #책을 안가져왔음
for student in range(1, 11) : # 1,2,3,4,5,6,7,8,9,10
    if student in absent :
        continue # 위 조건에 부합한다면, 다시 for문 재실행
    elif student in no_book : 
        print(f"오늘 수업 여기까지. {student}번은 교무실로 따라와.") 
        break # 종료
    print(f"{student}번, 책을 읽어봐")

# 한줄 for문 활용(리스트 컴프리헨션)
# 출석번호 1 2 3 4 앞에 100을 붙이기로함 -> 101, 102, 103, 104
students = [1,2,3,4,5]
print(students)
students = [i+100 for i in students] # i+100 을 해주고 리스트의 길이만큼 for문을 반복
print(students)

# 학생 이름을 길이로 변환
students = ["홍길동", "둘리", "또치"]
students = [len(i) for i in students]
print(students)

# 학생 이름을 대문자로 변환
students = ["hong", "dool", "ddoch"]
students = [i.upper() for i in students]
print(students)

# 실습
 #당신은 Cocoa 서비스를 이용하는 택시 기사님입니다.
# 50명의 승객과 매칭 기회가 있을 때, 총 탑승 승객 수를 구하는 프로그램을 작성하시오.
# 조건1 : 승객별 운행 소요 시간은 5분 ~ 50분 사이의 난수로 정해집니다.
# 조건2 : 당신은 소요 시간 5분 ~ 15분 사이의 승객만 매칭해야 합니다.
# 
# (출력문 예제)
# [0] 1번째 손님 (소요시간 : 15분)
# [ ] 2번째 손님 (소요시간 : 50분)
# [0] 3번째 손님 (소요시간 : 5분)
# ...
# [ ] 50번째 손님 (소요시간 : 16분)
# 총 탑승 승객 : 2 분#

from random import * # random모듈 import

cocoa = {i:randrange(5, 51) for i in range(1, 51)} #리스트 컴프리헨션으로 딕셔너리 초기화
print(cocoa) # 확인
count = 0 # 총 탑승 승객의 수를 count하기 위한 변수 초기화

# for문을 통해 딕셔너리의 items를 반복함 
# 이때 딕셔너리를 반복해서 items메서드를 사용하면 key,value를 한번에 얻어올 수 있음
for guest, time in cocoa.items() :
    if 5 <= time <= 15 : # 시간이 5분 이상 15분 사이의 승객 만 매칭
        count += 1 # 총 승객 수 카운팅
        print(f"[O] {guest}번째 손님 (소요시간 : {time}분)") # 5분 이상 15분 사이의 승객 출력문
    else : print(f"[ ] {guest}번째 손님 (소요시간 : {time}분)") # 15분 이상의 승객 출력문
print(f"총 탑승 승객 : {count}분") # 총 승객 출력 문

