# 함수
# Java에서의 메서드 정의와 비슷한 역할을 함 def키워드를 통해서 함수가 정의됨
#

#함수 생성
def open_account():
    print("새로운 계좌가 생성되었습니다.")
open_account() # 함수 호출

#함수의 재정의도 가능
# Java에서는 오버로딩을 통해서 같은 이름의 매개변수만 다른 여러개의 메서드를 생성할 수 있지만
# 파이썬은 같은 함수명을 사용하게 되면 새로운 데이터로 덮어씌워지게됨 
def open_account() : 
    print("새로 다시 정의된 함수로 변경")        
open_account()

# 전달값과 반환값
def deposit(balance, money) : # 입금
    print(f"입금이 완료되었습니다. 잔액은 {balance+money} 원입니다.")
    return balance + money

def witdraw(balance, money) :
    result = 0 # 반환 변수
    if balance >= money : #잔액이 출금보다 많으면
        print(f"출금이 완료되었습니다. 잔액은 {balance - money}원 입니다.")
        result = balance - money
    else : 
        print (f"출금이 완료되지 않았습니다. 잔액은 {balance}원 입니다.")
        result = balance
    return result
def withdraw_night(balance, money) : #저녁에 출금
    commission = 100 #수수료 100원
    return commission, balance - money - commission    
balance = 0 # 잔액
balance = deposit(balance, 1000)
# balance = witdraw(balance, 500)
commission, balance = withdraw_night(balance, 500)
print(f"수수료는{commission}원 이며, 잔액은{balance}원 입니다.")
        
# 기본값
def profile(name, age, main_lang) :
    print(f"이름 : {name}\n나이 : {age}\n주 사용 언어 : {main_lang}")

profile("홍길동", 20, "Python")            
profile("둘리", 25, "Java")

#같은 학교 같은 학년 같은 반 같은 수업.
#만약 값을 안넣었을 경우 인자값 = 데이터가 없을 경우의 값 을 통해 기본값 셋팅 가능
def profile(name, age = 17, main_lang = "Python") :
    print(f"이름 : {name}\n나이 : {age}\n주 사용 언어 : {main_lang}")

profile("홍길동")    
profile("또치")

# 키워드 값
# 키워드 값을 통해서 파라미터의 순서 상관없이 데이터를 입력가능
# 예시 : 파라미터값과 동일한 키워드 = 넣을 데이터값
def profile(name, age, main_lang) :
    print(name, age, main_lang)

profile(name ="홍길동", main_lang= "Python", age = 20)    
profile(age = 20, main_lang="Java", name= "길동이")

# 가변 인자

# def profile(name, age, lang1, lang2, lang3, lang4, lang5) :
#     print(f"이름 : {name}\n나이 : {age}")
#     print(lang1,lang2,lang3,lang4,lang5)

# *인자는 여러 자료형을 담을 수 있다
def profile(name, age, *language) :
    print(f"이름 : {name}\n나이 : {age}")
    for lang in language :
        print(lang, end = " ")
    print()
skile = ["Python", "Java", "C", "C++", "C#" , "JavaScript"]    
profile("홍길동", 20, skile,"여러가지","가능")

# **인자(가변 키워드 인자)는 딕셔너리형태로 담을 수 있다.
def profile(name, age, **language) :
    print(f"이름 : {name}\n나이 : {age}")
    for key, value in language.items() :
        print("키값:",key,"벨류값:",value, end = " ")
    print()
profile("홍길동", 20, back = "Python" , back2 = "Java")

# 지역변수 & 전역변수

gun = 10

def checkpoint(soldiers) : #경계근무
    global gun # global키워드를 사용해서 외부에 있는 gun변수 사용
    gun = gun - soldiers
    print(f"[함수  내] 남은 총 : {gun}")

# 지역 변수의 값을 return 을 활용해 수정할 수 있음
def checkpoint_ret(gun, soldiers) :
    gun = gun - soldiers # 함수내의 
    print(f"[함수  내] 남은 총 : {gun}")
    return gun
print (f"전체 총 : {gun}")
checkpoint(2) # 2명이 경계 근무를 나감

# return값을 이용해서 gun변수 데이터를 수정
gun = checkpoint_ret(gun, 2)

print (f"전체 총 : {gun}")

#실습
#표준 체중을 구하는 프로그램을 작성
# (성별에 따른 공식)
# 남자 : 키(m) x 키(m) x 22
# 여자 : 키(m) x 키(m) x 21
# 
# 조건 1 : 표준 체중은 별도의 함수 내에서 계산
#  * 함수명 : std_weight
#  * 전달값 : 키(height), 성별(gender)
# 조건 2 : 표준 체중을 소수점 둘째자리까지 표시
# 
# (출력 예제)
# 키 175cm 남자의 표준 체중은 67.38kg 입니다.#

def std_weigth(height, gender) : #함수 선언 전달값은 키, 성별
    weight = 0 # return할 변수
    if gender == "남자" : #만약 성별이 남자일 경우 다음 로직 실행
        # cm를 m으로 변환 후 실수로 변환하여 계산
        weight = round(float(int(height) / 100) * float(int(height) / 100) * 22 , 2)
    elif gender == "여자" : # 만약 성별이 여자일 경우 다음 로직 실행
         # cm를 m으로 변환 후 실수로 변환하여 계산
         weight = round(float(int(height) / 100) * float(int(height) / 100) * 21 , 2)
    return height,gender,weight

gender = input("성별이 어떻게 되시나요?")
height = input("키는 어떻게 되시나요?")
height,gender,weight = std_weigth(height,gender)
print(f"키{height}cm {gender}의 표준 체중은 {weight}kg 입니다.")