# 모듈
# 유지보수와 재사용이 용이함
# 영화관 모듈

# 일반 가격
def price(people) :
    print(f"{people}명 가격은 {people * 10000}원 입니다.")

# 조조 할인 가격
def price_morning(people) :
    print(f"{people}명 조조 할인 가격은 {people * 6000}원 입니다.")

# 군인 할인 가격
def price_soldier(people) :
    print(f"{people}명 군인 할인 가격은 {people * 4000}원 입니다.")