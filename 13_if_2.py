temp = int(input("기온은 어때요? ")) #input은 항상 문자열로 나오므로 int로 숫자형으로 변경시켜줌
if 30 <= temp:
    print("너무 더우니 나가지 마세요")
elif 10 <= temp and temp < 30:
    print("괜찮은 날씨에요")
elif 0 <= temp < 10:
    print("외투를 챙기세요")
else:
    print("너무 추우니 나가지 마세요")