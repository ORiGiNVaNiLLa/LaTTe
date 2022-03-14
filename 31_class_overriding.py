# 상속과 다중 상속에 대하여

# 일반 유닛
class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed

    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]".format(self.name, location, self.speed))


# 공격 유닛
class AttackUnit(Unit): # 공격 유닛 클래스가 일반 유닛 클래스를 상속 받음
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage

    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]".format(self.name, location, self.damage))

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))


# 날 수 있는 기능을 가진 클래스
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]".format(name, location, self.flying_speed))

# 공중 공격 유닛 클래스
class FlyableAttackUnit(AttackUnit, Flyable): # ---> AttackUnit과 Flyable 클래스를 상속받는 역할만 함
    def __init__(self, name, hp, damage, flying_speed): # ---> 여기서부터 상속 받은 애들 초기화 시켜줌
        AttackUnit.__init__(self, name, hp, 0, damage)
        # FlyableAttackUnit 클래스에 이미 Flying_speed가 정의 됐으므로 AttackUnit 클래스의 speed 값 0으로 입력
        Flyable.__init__(self, flying_speed)

    def move(self, location): # Unit 클래스의 move 함수가 아닌 FlyableAttackUnit 클래스의 move 함수를 새롭게 정의해줌
        print("[공중 유닛 이동]")
        self.fly(self.name, location)

# 벌쳐
vulture = AttackUnit("벌쳐", 80, 10, 20)

# 배틀크루저
battlecruiser = FlyableAttackUnit("배틀크루저", 500, 25, 3)

vulture.move("11시")
# battlecruiser.fly(battlecruiser.name,"9시")
battlecruiser.move("9시")