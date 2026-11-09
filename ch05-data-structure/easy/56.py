# tuple도 list처럼 `point[0]`, `point[1]` 인덱스로 원소에 접근합니다.
x = int(input())
y = int(input())

# 두 정수를 한 줄에 하나씩 입력받기
point = (x, y)
# x값 출력하기
print(f"x: {point[0]}")
# y값 출력하기
print(f"y: {point[1]}")