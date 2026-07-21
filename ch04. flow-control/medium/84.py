# 첫 번째 입력을 minimum으로 두고 나머지와 비교하세요.

# 첫 번째 입력을 minimum로 두기
minimum = int(input())
# 첫 번쨰 입력을 받았으니 남은 정수 4개 반복하기
for i in range(4):
    # 새 정수 입력받기
    new_num = int(input())

    # 만약 새로 입력받은 정수가 최소값보다 작다면
    if new_num < minimum:
        # 그 정수가 최소값으로 저장되기
        minimum = new_num
# 최소값 출력하기
print(f"최소값: {minimum}")