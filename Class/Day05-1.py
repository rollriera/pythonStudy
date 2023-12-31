# 실습 스타크래프트 게임
from random import *

class Unit : 
    def __init__(self, name, hp, speed) :
        
        self.name = name
        self.hp = hp
        self.speed = speed
        print(f"{name} 유닛이 생성되었습니다.")

    def move(self, location) :
        print("[지상 유닛 이동]")
        print(f"{self.name} : {location} 방향으로 이동합니다. [속도 {self.speed}]")

    def damaged(self, damage) :
         print(f"{self.name} : {damage} 데미지를 입었습니다. ")
         self.hp -= damage
         print(f"{self.name} : 현재 체력은 {self.hp} 입니다.")
         if self.hp <= 0 :
            print(f"{self.name} : 파괴되었습니다.")


class AttackUnit(Unit) :
    def __init__(self, name, hp, speed, damage) :
        Unit.__init__(self, name, hp, speed)
        self.damage = damage        

    def attack(self, location) :
        print(f"{self.name} : {location} 방향으로 적군을 공격 합니다.\
              [공격력 {self.damage}]")   

# 마린            
class Marine(AttackUnit) :
    def __init__(self):
        super().__init__("마린", 40, 1, 5)

    # 스팀팩 : 일정 시간 동안 이동 및 공격 속도를 증가, 체룍 10 감소
    def stimpack(self) :
        if self.hp > 10 :
            self.hp -= 10
            print(f"{self.name} : 스팀팩을 사용합니다.(HP 10 감소)")
        else : print(f"{self.name} : 체력이 부족하여 스팀팩을 사용하지 않습니다.")

class Tank(AttackUnit) :
    # 시즈 모드 : 탱크를 지상에 고정시켜, 더 높은 파워로 공격 가능
    seize_developed = False

    def __init__(self):
        super().__init__("탱크", 150, 1, 35)
        self.seize_mode = False       

    def set_seize_mode(self) :
        if Tank.seize_developed == False : return

        # 현재 시즈모드가 아닐 때 -> 시즈모드 
        if self.seize_mode == False :
            print(f"{self.name} : 시즈모드로 전환합니다.")
            self.damage *= 2
            self.seize_mode = True
        
        # 현재 시즈모드일 때 -> 시즈모드 해제 
        else :
            print(f"{self.name} : 시즈모드를 해제합니다.")
            self.damage /= 2
            self.seize_mode = False

class Flybale :
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location) :
        print(f"{name} : {location} 방향으로 날아갑니다. [속도 {self.flying_speed}]") 

class FlyableAttackUnit(AttackUnit, Flybale) :
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self,name, hp, 0, damage) # 지상 speed는 0        
        Flybale.__init__(self, flying_speed)

    def move(self, location) :
        print("[공중 유닛 이동]")
        self.fly(self.name, location)

class Wraith(FlyableAttackUnit) :
    def __init__(self):
        super().__init__("레이스", 80, 20, 5)
        self.clocked = False #클로킹 모드 (해제 상태)

    def clocking(self) :
        if self.clocked == True :
            print(f"{self.name} : 클로킹 모드 해제합니다.")    
            self.clocked = False
        else :
            print(f"{self.name} : 클로킹 모드 설정 합니다.")    
            self.clocked = True

class BuildingUnit(Unit) :
    def __init__(self, name, hp, location):
        #Unit.__init__(self, name, hp, 0)
        super().__init__(name, hp, 0)
        self.location = location  

def game_start() :
    print("[알림] 새로운 게임을 시작합니다.")

def game_over() :
    print("Player : gg")
    print("[Player] 님이 게임에서 퇴장하셨습니다.")    

# 실제 게임 진행
game_start()

# 마린 3기 생성
m1 = Marine()
m2 = Marine()
m3 = Marine()

# 탱크 2기 생성
t1 = Tank()
t2 = Tank()

# 레이스 1기 생성
w1 = Wraith()

# 유닛 일괄 관리
attack_units = []
attack_units.append(m1)
attack_units.append(m2)
attack_units.append(m3)
attack_units.append(t1)
attack_units.append(t2)
attack_units.append(w1)

# 전군 이동
for unit in attack_units :
    unit.move("1시")

# 탱크 시즈모드 개발
Tank.seize_developed = True 
print("[알림] 탱크 시즈 모드 개발이 완료되었습니다.")

# 공격 모드 준비 (마린 : 스팀팩, 탱크 : 시즈모드, 레이스 : 클로킹)
for unit in attack_units :
    if isinstance(unit, Marine) :
        unit.stimpack()
    elif isinstance(unit, Tank) :
        unit.set_seize_mode()
    elif isinstance(unit, Wraith) :
        unit.clocking()

# 전군 공격
for unit in attack_units :
    unit.attack("1시")                

# 전군 피해
for unit in attack_units :
    unit.damaged(randint(5, 21)) # 공격은 랜덤으로 받음 (5 ~ 20)

# 게임 종료
game_over()

