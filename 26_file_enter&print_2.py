# 텍스트 파일 내용 불러오기 방법 1
# score_file = open("25_score.txt", "r", encoding="utf8")
# while True:
#     line = score_file.readline()
#     if not line:
#         break
#     print(line, end="")
# score_file.close()

# 텍스트 파일 내용 불러오기 방법 2
score_file = open("25_score.txt", "r", encoding="utf8")
lines = score_file.readlines() # 리스트 형태로 저장
for line in lines:
    print(line, end="")
score_file.close