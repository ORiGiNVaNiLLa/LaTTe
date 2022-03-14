# 사전 {}

cabinet = {3:"유재석", 100:"김태호"}
print(cabinet[3])
print(cabinet[100])

print(cabinet.get(3))
print(cabinet.get(5)) # ★★★ 대괄호: 에러 뜨면서 프로그램 종료 / get 함수: None 출력 후 아래 코드 이어 나감 ★★★
print(cabinet.get(5, "사용 가능"))
print("hi")

print(3 in cabinet) # True
print(5 in cabinet) # False


cabinet1 = {"A-3":"유재석", "B-100":"김태호"}
print(cabinet1.get("A-3"))
print(cabinet1.get("B-100"))

# 새 손님
print(cabinet1)
cabinet1["A-3"] = "김종국"
cabinet1["C-20"] = "조세호"
print(cabinet1)

# 손님 갔음
del cabinet1["A-3"]
print(cabinet1)

# key 정보만 출력
print(cabinet1.keys())
# value 정보만 출력
print(cabinet1.values())
# key, value 쌍으로 출력
print(cabinet1.items())

# 목욕탕 폐점
cabinet1.clear()
print(cabinet1)