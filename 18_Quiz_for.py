# 50명의 승객과 매칭 기회가 있을 때, 총 탑승 승객 수를 구하는 프로그램을 작성하라

# 조건1 : 승객별 운행 소요 시간은 5 ~ 50분 사이의 난수로 정해짐
# 조건2 : 당신은 소요 시간 5분 ~ 15분 사이의 승객만 매칭해야 함

# from random import *

# time = range(5, 51)
# print(type(time))
# time = list(time)
# print(type(time))

# print(time)
# shuffle(time)
# print(time)

# for passenger_time in time:
#     if 5 < passenger_time < 15
#     print("[O] {0}번째 손님 (소요시간 : {1})").format(passenger, time))


# 예시 정답
from random import *
count = 0 # 매칭된 승객 수
for i in range(1, 51): #1 ~ 50 의 수 (승객)
    time = randrange(5, 51)
    if 5 <= time <= 15:
        print("[O] {0}번째 손님 (소요시간 : {1})".format(i, time))
        count += 1
    else:
        print("[ ] {0}번째 손님 (소요시간 : {1})".format(i, time))

print("총 탑승 승객 : {0} 분".format(count))


