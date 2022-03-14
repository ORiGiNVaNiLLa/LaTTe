# print("대기번호: 1")
# print("대기번호: 2")
# print("대기번호: 3")
# print("대기번호: 4")

for waiting_no in [0, 1, 2, 3, 4]: # waiting_no 라는 변수에 0부터 순서대로 들어가면서 프린트 구문 출력
    print("대기번호 : {0}".format(waiting_no))

for waiting_no in range(5): # waiting_no 라는 변수에 0부터 순서대로 들어가면서 프린트 구문 출력
    print("대기번호 : {0}".format(waiting_no))

for waiting_no in range(1, 6): # waiting_no 라는 변수에 1부터 순서대로 들어가면서 프린트 구문 출력
    print("대기번호 : {0}".format(waiting_no))


starbucks = ["아이언맨", "토르", "그루트"]
for customer in starbucks:
    print("{0}, 커피가 준비되었습니다".format(customer))