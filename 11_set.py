# 세트(집합)
# 중복 안됨, 순서 없음
my_set = {1,2,3,3,3}
print(my_set)

Java = {"유재석", "양세형", "김태호"}
Python = set(["유재석", "박명수"]) # 다른 포멧의 set 정의

# 교집합 (Java와 Python을 모두 할 수 있는 개발자)
print(Java & Python)
print(Java.intersection(Python))

# 합집합 (Java나 Python을 할 수 있는 개발자)
print(Java | Python)
print(Java.union(Python))

# 차집합 (Java는 할수 있으나 Pythons은 할줄 모르는 개발자)
print(Java - Python)
print(Java.difference(Python))

# Python을 할 줄 아는 사람이 늘어남(집합 추가)
Python.add("김태호")
print(Python)

# 유재석이 Java 쓰는 법을 까먹음
Java.remove("유재석")
print(Java)