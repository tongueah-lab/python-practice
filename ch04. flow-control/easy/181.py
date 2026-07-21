# 시작단과 끝단을 입력받아 해당 범위의 구구단을 출력하세요.
start = int(input())
end = int(input())

# dan의 시작과 끝을 숫자를 반복한다
for dan in range(start, end + 1):
    # 구분하는 선을 만든다
    print(f"--- {dan}단 ---")
    # 입력된 단을 1부터 9까지 곱한다
    for i in range(1, 10):
        # 구구단 출력하기
        print(f"{dan} x {i} = {dan * i}")