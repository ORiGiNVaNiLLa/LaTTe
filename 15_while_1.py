customer = "토르"
index = 5
while index >= 1: # -------> 옆의 조건이 만족할 때까지 계속 반복
    print("{0}, 커피가 준비되었습니다. {1} 번 남았어요".format(customer, index))
    index = index - 1 # == index -= 1
    if index == 0:
        print("커피는 폐기처분 되었습니다.")

# 무한 루프
# customer = "아이언맨"
# index = 1
# while True:
#     print("{0}, 커피가 준비 되었습니다. 호출{1} 회".format(customer, index))
#     index += 1
