# 바깥 for문은 단, 안쪽 for문은 곱하는 수(1~9)입니다.
a, b = map(int, input().split())

# 시작 단 a와 끝 단 b를 세로로 반복하기
for dan in range(a, b + 1):
    # 새로운 단을 시작할 때마다 반복 출력하기
    print(f"--- {dan}단 ---")
    # 1부터 9까지 가로로 반복하기
    for multiplier in range(1, 10):
        # 세로 가로 곱해서 구구단 출력하기
        print(f"{dan} x {multiplier} = {dan * multiplier}")
    # 새로운 단이 출력될 때마다 한 줄씩 띄우기
    print()
