# 바깥 for는 각 글자, 안쪽 for는 n번 출력
text = input()
n = int(input())

# 문자열 반복하기
for char in text:
    # 글자 n번 반복하기
    for i in range(n):
        # 문자열 나란히 출력하기
        print(char, end="")
# 줄바꿈하기
print()
