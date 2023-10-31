# 클래스
# 객체 OOP(객체 지향 프로그래밍)의 핵심 개념 중 하나이다.
# 클래스는 객체를 생성하기 위한 설계도이며, 관련 데이터와 함수를
# 하나로 묶는 역할을한다.
class Animal :

    # __init__(생성자)
    def __init__(self, name, age) :

        # 맴버 변수
        self.name = name
        self.age = age
    # 메서드
    def speak(self) :
        print(f"안녕 나는 {self.name} 이라고해! 나이는 {self.age}살이야!")

# 클래스 호출
# 호출과 동시에 __init__ 실행됨
dog = Animal("뚱이", 2)

# 해당 클래스의 temp메서드 호출
dog.speak()

# 상속
# OOP의 개념 중 하나로 상속을 통해 새로운 클래스를 정의할 때,
# 이미 존재하는 클래스의 속성과 메서드를 상속 받을 수 있다.
# 즉 기존 모든 클래스인 Animal 클래스는 부모클래스
# 상속을 받는 Dog, Cat은 자식 클래스이다.
# 상속을 받음 으로써 부모 클래스를 통해 자식클래스를 관리하고
# 자식클래스는 상속 받은 부모 클래스의 기능을 사용할 수 있다.

# 상속
class Dog(Animal) :
    def __init__(self, name, age):
        #super().__init__(self)
        Animal.__init__(self, name, age)

    def speak(self) :
         print(f"안녕 나는{self.name}이고, 나이는{self.age}야!")
         print("그리고 나는 강아지야!")    

animals = Dog("뚱이" ,2)
animals.speak()               

# 다중 상속
class test1() :
    def __init__(self):
        print("test1의 생성자 호출")

    def show1(self) :
        print("test1의 메서드")

class test2() :
    def __init__(self) :
        print("test2의 생성자 호출")              
    
    def show2(self) :
        print("test2의 메서드")

class test3(test1,test2) :
    def __init__(self):
        test1.__init__(self)        
        test2.__init__(self)

    def show3(self) :
        self.show1()
        self.show2()

i = test3()
i.show3()    

# 메소드 오버라이딩
class overLoading() :
    def __init__(self) :
        print("부모 클래스의 생성자")

    def show(self) :
        print("부모클래스의 show메서드")

class overloading2(overLoading) :
    def __init__(self):
        super().__init__()

    def show(self) :
        print("자식 클래스의 show메서드")

i = overloading2()
i.show()                


#실습
#주어진 코드를 활용하여 부동산 프로그램을 작성하시오.
# (출력 예제)
# 총 3대의 매물이 있습니다.
# 강남 아파트 매매 10억 2010년
# 마포 오피스텔 전세 5억 2007년
# 송파 빌라 월세 500/50 2000년
# 
# [코드]
# class House :
#   #매물 초기화
#   def __init__ (self, location, house_type, del_type, price, completion_year) :
#       pass
# 
#   # 매물 정보 표시
#   def show_detail(self) :
#       pass#

class House :
  #매물 초기화
  def __init__ (self, location, house_type, del_type, price, completion_year) :
      self.location = location
      self.house_type = house_type
      self.del_type = del_type
      self.price = price
      self.completion_year = completion_year

  # 매물 정보 표시
  def show_detail(self) :
      print(self.location,self.house_type,self.del_type,self.price,self.completion_year)

print("매물 등록 시스템")
info = []
for i in range(0 ,3) :

    location = input("위치 : ")
    house_type = input("타입 : ")
    del_type = input("판매 조건 : ")
    price = input("금액 : ")
    completion_year = input("완공년도 : ")
    info.append(House(location, house_type, del_type, price, completion_year))

print(f"총 {len(info)}대의 매물이 있습니다.")
for i in info :
    i.show_detail()
