absent = [2, 5] # 결석
for student in range(1, 11):
    if student in absent:
        continue # 계속해서 다음 반복문을 진행
    print("{0}, 책을 읽어봐".format(student))

# ------------------------------------------------------------------------------

absent = [2, 5] # 결석
no_book = [7]
for student in range(1, 11):
    if student in absent:
        continue
    elif student in no_book:
        print("오늘 수업 여기까지. {0}는 교무실로 따라와".format(student))
        break # 바로 반복문을 종료하고 끝냄
    print("{0}, 책을 읽어봐".format(student))
