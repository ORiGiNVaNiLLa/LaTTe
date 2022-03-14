from random import* # 유닛 피해량 난수로 적용하기 위해 부름

# 일반 유닛
class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
        print("{0} 유닛이 생성되었습니다".format(self.name))

    def move(self, location):
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]".format(self.name, location, self.speed))

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))


# 공격 유닛
class AttackUnit(Unit): # 공격 유닛 클래스가 일반 유닛 클래스를 상속 받음
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage

    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]".format(self.name, location, self.damage))

# ---------------------------------------------------------------------------------------------------------#

# 마린 클래스
class Marine(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self, "마린", 40, 1, 5)

    # 스팀팩
    def stimpack(self):
        if self.hp >10:
            self.hp -= 10
            print("{0} : 스팀팩을 사용합니다(hp 10 감소)".format(self.name))
        else:
            print("{0} : 체력이 부족하여 스팀팩을 사용하지 않습니다".format(self.name))


# 탱크 클래스
class Tank(AttackUnit):
# 시즈모드
    seize_developed = False # 시즈모드 개발여부

    def __init__(self):
        AttackUnit.__init__(self, "탱크", 150, 1, 35)
        self.seize_mode = False

    def set_seize_mode(self):
        if Tank.seize_developed == False:
            return

        if self.set_seize_mode == False:
            print("{0} : 시즈모드로 전환 합니다.".format(self.name))
            self.damage *= 2 # 시즈모드일때 공격력 2배
            self.seize_mode = True # 시즈모드가 True로 변경 -> 시즈모드 함수가 한번더 호출될때 True 상태임
        
        else:
            print("{0} : 시즈모드를 해제 합니다.".format(self.name))
            self.damage /= 2 # 시즈모드 해제로 공격력 반감
            self.seize_mode = False # 시즈모드가 False 로 변경 -> 시즈모드 함수가 한번더 호출될때 False 상태임

# ---------------------------------------------------------------------------------------------------------#

# 날 수 있는 기능을 가진 클래스
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]".format(name, location, self.flying_speed))

# 공중 공격 유닛 클래스
class FlyableAttackUnit(AttackUnit, Flyable): # ---> AttackUnit과 Flyable 클래스를 상속받는 역할만 함
    def __init__(self, name, hp, damage, flying_speed): # ---> 여기서부터 상속 받은 애들 초기화 시켜줌
        AttackUnit.__init__(self, name, hp, 0, damage) # 지상 speed 값 0
        Flyable.__init__(self, flying_speed)

    def move(self, location): # Unit 클래스의 move 함수가 아닌 FlyableAttackUnit 클래스의 move 함수를 새롭게 정의해줌
        self.fly(self.name, location)

# ---------------------------------------------------------------------------------------------------------#

# 레이스
class Wraith(FlyableAttackUnit):
    def __init__(self): # -> __init__ 함수 초기화
        FlyableAttackUnit.__init__(self, "레이스", 80, 20, 5)
        self.clocked = False # 처음에는 클로킹 해제 상태

    def clocking(self):
        if self.clocked == True:
            print("{0} : 클로킹 모드를 해제합니다.".format(self.name))
            self.clocked = False
        else:
            print("{0} : 클로킹 모드를 적용합니다.".format(self.name))
            self.clocked = True

# ----------------------------------------보조함수-------------------------------------------------------------#

def game_start():
    print("게임을 시작합니다")

def game_over():
    print("플레이어 : GG")
    print("플레이어님이 게임에서 퇴장하셨습니다.")

# ----------------------------------------게임 시작-------------------------------------------------------------#
game_start()

# 유닛 생성 > 마린3 ,탱크 2, 레이스1
m1 = Marine()
m2 = Marine()
m3 = Marine()
t1 = Tank()
t2 = Tank()
w1 = Wraith()

# 유닛 일괄 관리를 위해 리스트 생성
attack_unit = []
attack_unit.append(m1)
attack_unit.append(m2)
attack_unit.append(m3)
attack_unit.append(t1)
attack_unit.append(t2)
attack_unit.append(w1)

# 전군 이동하면서 시즈모드 개발
for unit in attack_unit:
    unit.move("1시")
    Tank.seize_developed = True
    print("[알림] : 탱크 시즈모드 개발이 완료되었습니다.")

# 공격모드 준비 : 마린 스팀팩, 탱크 시즈모드, 레이스 클로킹 적용
 # isinstance -> 리스트 안에 유닛의 클래스가 마린일 경우 스팀팩, 탱크일 경우 시즈모드, 레이스일 경우 클로킹을 하라
for unit in attack_unit:
    if isinstance(unit, Marine):
        unit.stimpack()
    elif isinstance(unit, Tank):
        unit.set_seize_mode()
    elif isinstance(unit, Wraith):
        unit.clocking()

# 전군 공격
for unit in attack_unit:
    unit.attack("1시")

# 전군 피해
for unit in attack_unit:
    unit.damaged(randint(5, 21)) # 5~ 20 사이의 피해량 설정

# 게임 종료
game_over()