# 리스트 : 순서를 가지는 객체의 집합 [] Java의 배열
# Java에서는 배열과 컬랙션 객체인 ArrayList로써의 분배가 있지만 Python에서는 리스트라고 불리며 자바에서의 
# 배열과는 리스트의 index값이 동적으로 증가함

# 지하철 칸별로 10명, 20명, 30명 ~
subway = [10,20,30]
print(subway)

#Java에서는 Heap영역에 저장된 배열의 주소값이 출력되지만 Python은 배열의 데이터를 바로 출력
print(subway)

# 직접 index값으로도 접근이 가능함
print(subway[0])
print(subway[1])
print(subway[2])

# index 메서드를 이용해서 내가 원하는 값의 index값을 출력할 수도 있음
print(subway.index(20))

#append 메서드를 이용해서 데이터 추가도 가능함 append함수를 사용하면 항상 맨 뒤에 등록되게됨
subway.append(40)
print (subway)

#insert 메서드를 이용해서 추가하고 싶은 데이터의 위치도 지정할 수 있음
#예시 : subway.insert(index 위치값 , 추가하고싶은 데이터)
subway.insert(0 , 20)
print(subway)

#pop이라는 메서드를 통해서 데이터 한개씩만 제거 특정 index의 데이터도 제거 가능
print(subway.pop()) # 파라미터 값을 적지 않으면 뒤에서부터 하나만 제거 하고 제거한 데이터를 출력해줌
print(subway.pop(1)) # index값을 parameter로 넣고 삭제도 가능
print(subway)

#count 메서드를 통해서 동일한 데이터값이 몇개가 존재하는지 확인도 가능
print(subway.count(20))

#sort 메서드를 이용해서 오름차순 정렬도 가능
num_list = [5,2,4,3,1]
num_list.sort()
print(num_list)

#reverse 메서드를 이용해서 내림차순 정렬도 가능
num_list.reverse()
print(num_list)

# clear 메서드를 통해서 배열안에 있는 데이터도 삭제 가능
num_list.clear()
print(num_list)

#다양한 자료형 함께 사용 가능
num_list = [5,2,4,3,1]
mix_list = ["Python", 20, True]
print(mix_list)

#extend메서드를 이용해서 리스트 확장 가능
mix_list.extend(num_list)

#리스트를 확장했다고 접근 방법이 달라지진 않음
print(mix_list[0])
print(mix_list[1])
print(mix_list[2])
print(mix_list[3])
print(mix_list[4])
print(mix_list[5])
print(mix_list[6])
print(mix_list[7])

#딕셔너리 (key , value) Java에서의 Map 형식과 비슷함 int 나 String 타입으로도 키값을 선언 가능
cabinet = {1: "강아지", 3:"고양이"}

#대괄호 안에다가 키값을 입력하면 키값에 맵핑된 데이터가 출력됨
print(cabinet[3]) # Java에서의 Map.get(3);
print(cabinet[1])

print(cabinet.get(3)) #Java와 동일하게 get메서드가 있음

#주의점
#대괄호 안에다가 없는 키값을 입력했을 때는 Exception이 발생 되며 프로그램이 종료되지만
# print(cabinet[5])
#get메서드를 이용하면 None로 출력되면서 프로그램이 그대로 실행됨
print(cabinet.get(5))
print("test")

#만약 키값이 없는 경우에는 다른 방법으로도 처리가능
print(cabinet.get(5, "만약 해당 키값이 없으면 이 문장을 출력"))

# 해당 딕셔너리에 내가 찾고싶은 키가 있는지 확인도 가능
# 예시 : 키값 in 변수명 boolean타입으로 결과 반환
print(3 in cabinet) #True
print(5 in cabinet) #False

#딕셔너리에 새로운 데이터를 추가
# 예시 : 변수명[새로운 키값] = 맵핑할 데이터 기입
# 데이터를 추가하고 중복된 키값으로 만약 데이터를 넣는다고 한다면 
# 해당 키에 맵핑된 기존 데이터를  새로운 데이터로 덮어씌우게됨

cabinet[5] = "병아리" # 새로운 키 와 value 맵핑
print(5 in cabinet) # 정상적으로 등록됬는지 검사
print(cabinet) # 결과 출력
cabinet[5] = "부엉이" # 기존 키에 새로운 데이터 덮어씌우기
print(cabinet) # 전체 데이터 조회
print(cabinet.get(5)) # 덮어씌운 데이터 확인

# del 예약어를 이용하여 특정 데이터나 변수 리스트의 요소를 삭제할 수 있다.
del cabinet[5] # del 예약어 사용해서 딕셔너리의 데이터 삭제
# 정상적으로 삭제 됬는지 검증
print(5 in cabinet)
print(cabinet.get(5))

# 해당 딕셔너리에 키값 전체 조회 keys 메서드 사용(Java의 keyset 메서드와 동일)
print(cabinet.keys())

# 해당 딕셔너리에 value 전체 조회 values메서드 사용(Java와 동일)
print(cabinet.values())

# 해당 딕셔너리의 key, value 전부 조회 items 메서드 이용(Java의 entrySet 메서드와 동일)
print(cabinet.items())

# clear 메서드를 이용해서 해당 딕셔너리의 key, value 값을 삭제
cabinet.clear()
print(cabinet)

# 튜플 (불변 데이터 타입) 
# 예시 : list("test1" , "test2")
# 리스트와 다르게 내용변경이나 추가 불가
# 대신 속도가 빠르다?
# 변경되지 않는 목록을 이용할때 사용

menu = ("돈까스" , "치즈까스")
print(menu[0])
print(menu[1])

# menu.add("생선까스") 추가 불가능 Exception 출력

# name = "홍길동"
# age = 20
# hobby = "코딩"
# print(name,age,hobby)
#위 변수들을 튜플을 통해서 한번에 선언 가능
(name, age, hobby) = ("홍길동", 20, "코딩")
print(name, age, hobby)

c = (1,2,3)
d = (3,1,5)
print(c*5) # 곱셈 가능(기존데이터에서 곱셈이 되는 방식은 아님 기존의 데이터가 곱한 수만큼 반복됨)
print(c[0]) # 인덱싱 가능
print(c[1:]) #슬라이싱 가능

#덧셈 가능(덧셈을 이용해서 튜플 확장이 가능)
a = c + d 
print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[4])
print(a[5])

# 세트
# 중복 불가, 순서 x
my_set = {1,2,3,3,3} #중복되는 값은 무시되어 적용됨
print(my_set)

java = {"홍길동", "둘리", "나나"}
python = set(["보라돌이", "뚜비", "홍길동"])

# 교집합 (java 와ㅏ python을 모두 할 수 있는 개발자)
print(java & python)
print(java.intersection(python)) # 교집합을 반환하는 메서드

# 합집합 (java나 python을 할 수 있는 개발자)
print(java | python)
print(java.union(python)) # 합집합을 반환하는 메서드

# 차집합 (java는 할 수 있지만 python은 할 줄 모르는 개발자)
print(java - python)
print(java.difference(python)) #차집합을 반환하는 메서드

python.add("짱구") # 값을 추가도 가능
print(python)

java.remove("둘리") #remove메서드를 통해서 자료형을 삭제 시키기 가능
java.clear() # clear 메서드 사용 가능
print(java)

# 자료구조의 변경
menu = {"커피" , "우유", "주스"}
print(type(menu))

menu = list(menu) #list type으로 변경
print(type(menu))

menu = tuple(menu)
print(type(menu))

menu = set(menu)
print(type(menu))

#실습
#당신의 학교에서는 파이썬 코딩 대회를 주최합니다.
# 참석률을 높이기 위해 댓글 이벤트를 진행하기로 하였습니다.
# 댓글 작성자들 중에 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰을 받게 됩니다.
# 추첨 프로그램을 작성하시오.
# 
# 조건1 : 편의상 댓글은 20명이 작성하였고 아이디는 1~20 이라고 가정
# 조건2 : 댓글 내용과 상관 없이 무작위로 추첨하되 중복 불가
# 조건 3 : random 모듈의 shuffle 과 sample 을 활용
# 
# (출력 예제)
# -- 당첨자 발표 --
# 치킨 당첨자 : 1
# 커피 당첨자 : [2, 3, 4]
# -- 축하합니다 --#

from random import * #random 모듈을 import
user = range(1, 21) # 1부터 20 까지 숫자를 생성
user = list(user)
shuffle(user) #무작위로 섞는 메소드
print(user)

# sample를 통해 내가 무작위로 추출할 list, set 자료형을 명시하고 몇개의 요소를 추출 할지 기입 한다
chhiken = sample(user, 1)
coffe = sample(user, 3)
print(f"-- 당첨자 발표 --\n치킨 당첨자 : {chhiken} \n커피 당첨자 : {coffe} \n -- 축하합니다 --")

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


