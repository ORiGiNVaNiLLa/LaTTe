gun = 10

def checkpoint(soldiers): # 경계근무 함수에 병사수가 변수
    gun = 20
    gun = gun - soldiers
    print("[함수내] 남은 총: {0}".format(gun))

print("전체 총: {0}".format(gun)) # 첫 줄 10 출력
checkpoint(2) # checkpoint 함수 내 gun 20 - 2 = 18 출력
print("남은 총: {0}".format(gun)) # 첫 줄 10 출력


###########################################################################

gun = 10

def checkpoint(soldiers): # 경계근무
    global gun # 전역 공간에 있는 gun 사용
    gun = gun - soldiers
    print("[함수내] 남은 총: {0}".format(gun))

print("전체 총: {0}".format(gun)) # 첫 줄 10 출력
checkpoint(2) # checkpoint 함수 내 gun 10 - 2 = 8 출력
print("남은 총: {0}".format(gun)) # 함수 거치고 다시 정의된 gun 8 출력

###########################################################################

gun = 10

def checkpoint_return(gun, soldiers): # 경계근무
    gun = gun - soldiers # 전역 공간에 있는 gun 사용
    print("[함수내] 남은 총: {0}".format(gun))
    return gun

print("전체 총: {0}".format(gun)) # 첫 줄 10 출력
gun = checkpoint_return(gun, 2) # checkpoint_return 함수에서 나온 gun 10 - 2 = 8을 새로운 gun으로 지정
print("남은 총: {0}".format(gun)) # 함수 거치고 다시 정의된 gun 8 출력