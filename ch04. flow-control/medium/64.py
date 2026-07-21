# chr(65)는 'A', chr(65+1)은 'B'입니다.
n = int(input())

# 행 n번 반복하기
for i in range(n):
    # 열 i까지 반복하기
    for j in range(i + 1):
        # 알파벳 출력하기
        print(chr(65 + j), end="")
    # 줄바꾸기
    print()