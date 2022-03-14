# 내 풀이

def std_weight(height, gender):
    if gender == "man":
        man_std_weight = height*0.01 * height*0.01 * 22
        print("키 {0}cm 남자의 표준 체중은 {1}kg 입니다.".format(height, man_std_weight))
    else:
        woman_std_weight = height*0.01 * height*0.01 * 21
        print("키 {0}cm 여자의 표준 체중은 {1}kg 입니다.".format(height, woman_std_weight))


std_weight(162, "woman") # checkpoint_return 함수에서 나온 gun 10 - 2 = 8을 새로운 gun으로 지정


############# 예시 정답 ###############
def std_weight(height, gender):
    if gender == "man":
        return height * height * 22
    else:
        return height * height * 21

height = 175 # cm 단위
gender = "man"
weight = std_weight(height / 100, gender)
weight =round(weight, 2)

print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height, gender, weight))