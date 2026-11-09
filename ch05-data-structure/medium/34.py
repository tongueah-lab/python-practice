# 슬라이스 할당은 `lst[a:b] = 새로운_시퀀스` 형태로 사용합니다. 길이가 달라도 OK.
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a = int(input())
b = int(input())

# 슬라이싱 a부터 b까지는 0으로 바꾸기
data[a:b] = [0]
# 출력하기
print(" ".join(map(str, data)))