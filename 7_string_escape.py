# 문장 탈출

# \n : 줄바꿈
print("백문이 불여일견\n백견이 불여일타")

# 저는 "나도코딩"입니다.
print('저는 "나도코딩"입니다.')
print("저는 \"나도코딩\" 입니다.") # \" \" 와 \' \' : 문장 내에서 따옴표로 사용 가능

# \\ : 문장 내에서는 \ 1개로 변함
print("C:\\Users\\LEEHGI\\Desktop\\pythonWorkspace")  # 경로 지정 때 \ 2개씩으로 구분해주면 가능
# \r : 커서를 맨 앞으로 이동
print("Red Apple\rPine")
# \b : 백스페이스 역할(한 글자 삭제)
print("Redd\bApple")
# \t : 탭 기능
print("Red\tApple")


# 퀴즈
url = "http://naver.com"
# password = password[7:12] + len(password) + password.count("e") + "!"
my_str = url[7:12]
password = my_str[0:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
print("생성된 비밀번호 : {}".format(password))


# 예시 정답
# url = "http://youtube.com"
# my_str = url.replace("http://", "")
# print(my_str)
# my_str = my_str[:my_str.index(".")] # my_str[0:5] -> 0 ~ 5 직전까지만
# print(my_str)
# password = my_str[0:3] + str(len(my_str)) + str(my_str.count("e")) +"!"
# print("{0}의 비밀번호는 {1}입니다.".format(url, password))