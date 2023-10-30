# 파이썬 숫자 자료형
print(5)
print(-10)
print(3.14)

# 파이썬 boolean
print(5 < 10);
print(not True); #파이썬에선 not도 붙일수있음 첫 시작 글은 대문자로 써줘야함

# 파이썬 변수
#예시 = 애완동물 소개
animal = "강아지"
name = "연탄"
age = 4
hobby = "산책"
is_adult = age >= 3
print("우리집" + animal + "의 이름은" + name + "이에요")
hobby = "공놀이"
print(name,"이 는 ", str(age), "살이며, ",hobby, "를 아주 좋아해요") #파이썬에선 문자열의 연결을 콤마로 연결가능 (','로 작성하게 되면 공백이 하나 포함되게됨)

# 파이썬의 연산자
#산술 연산자
print(2**3) # 2^3 지수연산
print(10//2) #몫 연산
print(10%2) #나머지 연산

#논리 연산자 and 와 or 연산자에서 "and" 나 "or"을 기입해서 사용가능
print(not(1 != 3))
print((3 > 0) & (3 < 5)) # 비트 연산자 &
print((3 > 0) and (3 < 5)) # 논리연산자 and

print((3 > 0) or (3 > 5)) # 논리 연산자 or
print((3 > 0) | (3 > 5)) # 비트 연산자

#숫자 처리 함수
print(abs(-5)) #절대값 함수
print(pow(4, 2)) # 4*4
print(max(5, 12)) #최대값 반환 함수
print(min(5, 12)) #최소값 반환 함수
print(round(3.1)) #반올림 함수

from math import * #math라이브러리 안에있는 모든것을 사용
print(floor(-3.9)) #내림
print(ceil(3.14)) #올림
print(sqrt(16)) #제곱 (음수를 넣게될 경우에는 에러를 출력)

#랜덤 함수
from random import *

print(random()) # 0.0 ~ 1.0 미만의 임의의 값 생성
print(random() * 10) # 0.0 ~ 10.0 미만의 임의의 값을 생성해줌
print(int(random() * 10) + 1) # int함수를 사용하면 실수에서 정수로 나타남 

print(type(int(random() * 45 + 1))) # 1 ~ 45 이아의 임의의 값을 생성
print(randrange(1, 46)) # 1 ~ 46 미만의 임의의 값을 생성 위 코드의 식과 같은 행위를 하는 함수 randrange
print(randint(1, 45)) # 1 ~ 45 이하의 밍의의값을 생성해주는 함수

#실습 
# 월 4회 스터디를 하는데 3번은 온라인으로 하고 1번은 오프라인으로 하기로 했습니다. 아래 조건에 맞는 오프라인 모임 날짜를 정해주는 프로그램을 작성
#조건1 : 랜덤으로 날짜를 뽑아야함
#조건2 : 월별 날짜는 다름을 감안하여 최소 일수인 28 이내로 정함
#조건3 : 매월 1~3일은 스터디 준비를 해야 하므로 제외
#출력문 = "오프라인 스터디 모임 날짜는 매월 x 일로 선정되었습니다.#

studyDay = randrange(4, 29) #최소값 이상 최대값 미만의 함수인 randrange함수를 이용
# print("오프라인 스터디 모임 날짜는 매월" + studyDay + "일로 선정되었습니다.") 자바에선 에러출력 x(오버로딩)
print("오프라인 스터디 모임 날짜는 매월" + str(studyDay) + "일로 선정되었습니다.") #파이썬에서는 지원하지않음

#문자열
sentence = '나는 소년입니다'
print(sentence)
sentence2 = "파이썬 배우기"
print(sentence2)

#파이썬에서는 여러줄로된 문자열을 처리할때 삼중 따옴표 사용가능
sentence3 = """
안녕하세요 정말
반갑습니다.
"""
print(sentence3)

#슬라이싱
jumin = "990120-1234567"
print("성별 : " + jumin[7]) 
#index 값을 이용해 추출 자바에서는 (jumin.charAt(7) = 1) 하지만 자바에서는 지정index위치에 존재하지 않으면 에러를 출력

#index 값을 이용해 추출 자바에서는 (jumin.substring(0, 2) = 99)
print("연 : " + jumin[0:2]) 
print("월 : " + jumin[2:4])
print("일 : " + jumin[4:6])

print("생년월일 : " + jumin[:6]) # 처음부터 index 6 직전까지
print("뒤 7자리" + jumin[7:]) #index 7 부터 끝까지
print("뒤 7자리 (뒤에부터) : " + jumin[-7:]) # 맨 뒤에서 7번째부터 끝까지

#문자열 처리 함수
python = "Python is Amazing"
print(python.lower()) #자바에서는 toLowerCase()메서드
print(python.upper()) #자바에서는 toUpperCase()메서드

#자바에서는 Character.isUpperCase(jumin.charAt(0)) 0번째 위치의 문자를 
# char자료형으로 반환받은후 isUpperCase메서드를 통해 대문자인지 소문자인지 판별#
print(python[0].isupper())
print(len(python)) # python.length()와 동일
print(python.replace("Python" , "Java")) #자바와 동일

index = python.index("n") #자바에서의 python.indexOf("n") 특정 문자의 index값을 반환시켜줌
print(index)
index = python.index("n", index + 1) # python.indexOf("n" , python.indexOf("n")+1) 자바와 동일
print(index)

print(python.find("Java")) # 내가 원하는 값이 변수에 포함되지 않는 경우엔 -1로 뜨게됨 에러 출력되지 않음 index로 쓰게될 경우 오류 출력됨
print(python.count("n")) # 현 변수에서 내가 원하는 문자가 몇개가 있는지 int로 돌려줌

# 문자열 포맷

#방법 1 
# %d , %f, %c , %s를 활용한 문자열 수정
# %d 작성한 문자가 끝난 뒤에 붙혀줄 수 있음 대신 %d를 작성한 위치에 넣고싶은 원하는 숫자나 문자를 기입하고 앞에 %를 붙혀줘야함
# %d = int /%f = double / %s = String / %c = char 
print("나는 %d살입니다." % 20) 
print("오늘의 날씨는 %.1f도 입니다." % 20.8) #소숫 점 원하는 자릿수 까지 표시를 하고 싶으면 %.1(소수 자릿수)f
print("나는 %s을 좋아해요." % "파이썬")
print("Apple 은 %c로 시작해요." % "A")

print("나는 %s색과 %s색을 좋아해요." % ("파란", "빨간")) # 두개도 입력가능
print("나는 %s색을 가진 물건 %d개를 가지고싶어요." % ("보라" , 8))

#방법 2
# format함수 이용 기호는 {}중괄호 사용
print("나는 {}살입니다.".format(20))
print("나는 {}색과 {}색을 좋아해요.".format("파란", "빨간"))
print("나는 {0}색과 {1}색을 좋아해요.".format("파란", "빨간"))
print("나는 {1}색과 {0}색을 좋아해요.".format("파란", "빨간")) #index값을 지정해서 원하는 위치에 문자열 수정가능

#방법 3
# format함수 안에서 변수 정의
print("나는 {age}살이며, {color}색을 좋아해요.".format(age = 20, color = "빨간"))
print("나는 {age}살이며, {color}색을 좋아해요.".format(color = "빨간", age = 20))

# 방법 4
#변수를 선언 한 후에 내가 수정할 문자 맨앞에f를 붙혀넣고 중괄호안에 변수명 기입{} 방법3 에서 .format 선언만 빠지고 나머진 동일
age = 20
color = "빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요.")

#탈출 문자
# 자바에서도 동일하게 사용됨

# \n 줄바꿈
print("백문이 불여일견 \n 백견이 불여일타")

# \" \" , \' \'문장 내에서의 "" / ''
print("저는 \"빕스\"가 가고싶습니다.")

# \\ 문장내에서의 \ 
print("C:\\Users\\8426\\Desktop\\PythonStudy>")

# \r : 커서를 맨 앞으로 이동
print("Red Apple\rPine")

# \b : 백스페이스 (한 글자 삭제)
print("Redd\bApple")

# \t : 탭
print("Red\tApple")

# 문자열 조작 실습 
# http://naver.com 에서 nav51!로 변경
#규칙 1 : http:// 부분 제거 => naver.com
# 규칙 2 : 처음 만나는 점(.) 이후 부분 제거 => naver
# 규칙 3 : 남은 글자중 처음 세자리(nav) + 글자 수(5) + 글자 내 'e' 갯수(1) + "!"로 구성#
url = "http://naver.com"
url = "http://youtube.com"
url = url.replace("http://","")
url = url[:url.index(".")]
url = url[0:3]+str(len(url))+str(url.count("e"))+"!"
print(url)

