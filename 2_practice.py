# 1. 변수에 대해서
name = "해피"
animal = "고양이"
age = 4
hobby = "잠"
is_adult = age >= 3

print("우리집 " + animal + "의 이름은 " + name + "예요")
hobby = "공놀이"
#print(name + "는 " + str(age) + "살이며, " + hobby + "을 아주 좋아해요")
print(name, "는 ", age, "살이며, ", hobby, "을 아주 좋아해요")
print(name + "는 어른일까요? " + str(is_adult) )

# ★★★ 주석 적용 및 해제는 컨트롤 + 슬러시 ★★★

# 퀴즈
station = "사당"
print(station + "행 열차가 들어오고 있습니다.")


# 2. 연산자에 대해서
print(1+1) # 2
print(3-2) # 1
print(5*2) # 10
print(6/3) # 2

print(2**3) # 8
print(5%3) # 나머지 구하기 2
print(10%3) # 1
print(5//3) # 몫 구하기 1
print(10//3) # 3

print(10 > 3) # True
print(4 >= 7) # 4는 7보다 크거나 같다 False
print(10 <3) # False
print(5 <= 5) # True
print(3 == 3) # True
print(4 == 2) # False
print(7 == 3+4) # True
print(1 != 3) # 1은 3과 같지 않다 True
print(not(1 !=3)) # False

print((3 > 0) and (3 < 5)) # True
print((3 > 0) & (3 < 5)) # True

print((3 > 0) or (3 > 5)) # True
print((3 > 0) | (3 > 5)) # True

number = 2 + 3 * 4
print(number)
number = number + 2
print(number)
number += 2
print(number)
number *= 2
print(number)
number /= 2
print(number)
number -= 2
print(number)
number %= 5
print(number)