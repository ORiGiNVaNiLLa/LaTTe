# 자료구조의 변경
# 커피숍
menu = {"커피", "우유", "쥬스"}
print(menu, type(menu))

menu = list(menu)
print(menu, type(menu))

menu = tuple(menu)
print(menu, type(menu))

menu = set(menu)
print(menu, type(menu))


# 퀴즈

# 해결 팁
# from random import *
# lst = [1,2,3,4,5]
# print(lst)
# shuffle(lst)
# print(lst)
# print(sample(lst, 1))

# 예시정답
from random import *
users = range(1, 21) # 1 ~ 20까지 숫자 생성
print(type(users))
users = list(users) # 타입을 range에서 list로 바꿈 -> list용 함수를 사용하기 위해
print(type(users))

shuffle(users)
print(users)

winners = sample(users, 4)
print(winners)

print(" -- 당첨자 발표 -- ")
print("치킨 당첨자 : {0}".format(winners[0]))
print("커피 당첨자 : {0}".format(winners[1:]))
print(" -- 축하합니다 -- ")