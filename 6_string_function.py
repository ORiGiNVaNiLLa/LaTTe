# 문자열 처리 함수

python = "Python is Amazing"
print(python.lower()) # 문자를 다 소문자로
print(python.upper()) # 문자를 다 대문자로
print(python[0].isupper()) # 변수 문자의 첫글자가 대문자면 True
print(len(python))
print(python.replace("Python", "Java"))

index = python.index("n")
print(index)
index = python.index("n", index + 1) # index + 1 변수는 start 위치 입력
print(index)

print(python.find("n"))

print(python.find("Java")) # find는 원하는 값이 없을경우 -1 반환
# print(python.index("Java")) # index는 원하는 값이 없을경우 -1 반환
print("hi")

print(python.count("n"))


# 문자열 포멧

# print("a" + "b")
# print("a", "b")

# 방법1
print("나는 %d살입니다" % 20) # d는 정수값만 입력 가능
print("나는 %s을 좋아해요." % "파이썬") # s는 문자열
print("Apple 은 %c로 시작해요." % "A") # c는 문자

print("나는 %s살입니다" % 20) # s로 d, S, c 모두 대체 가능
print("나는 %s색과 %s색을 좋아해요." % ("파란", "빨간"))
# 방법2
print("나는 {}살입니다." .format(20))
print("sksms {}색과 {}색을 좋아해요." .format("파란", "빨간"))
print("sksms {0}색과 {1}색을 좋아해요." .format("파란", "빨간"))
print("sksms {1}색과 {0}색을 좋아해요." .format("파란", "빨간"))
# 방법3
print("나는 {age}살이며, {color}색을 좋아해요." .format(age = 20, color = "빨간"))
print("나는 {age}살이며, {color}색을 좋아해요." .format(color = "빨간", age = 20))
# 방법4
age = 20
color = "빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요") # f를 먼저 쓰고 쓰면 선언한 변수들 그대로 갖다 쓸 수 있음
 