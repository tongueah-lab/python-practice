# 정답 42. prev_diff=100 초기값.
treasure = 42
attempt = 0
prev_diff = 100

# 보물 찾기 인사말 출력하기
print("=== 보물 찾기 ===")
print("1~100 사이에 보물이 숨겨져 있습니다!")
print()

# 참이 될 때까지 반복하기
while True:

    # 값 입력받기
    num = int(input())
    # 도전할 때마다 횟수 세기
    attempt += 1
    # 입력 값과 정답 차 구하기
    diff = num - treasure
    # 절댓값으로 구하기
    if diff < 0:
        diff = -diff

    # diff==0:이면 보물과 축하인사 출력후 반복문 종료하기
    if diff == 0:
        print(f"보물을 찾았습니다! (시도: {attempt}회)")
        print(f"축하합니다! 총 {attempt}번 만에 보물을 찾았습니다!")
        break
    # diff 1~5: 뜨겁다고 출력하기
    elif 1 <= diff <= 5:
        print(f"뜨거워! 아주 가까워요! (시도: {attempt}회)")
    # diff 6~15: 따뜻하다고 출력하기
    elif 6 <= diff <= 15:
        print(f"따뜻해요! 근처에 있어요! (시도: {attempt}회)")
    # diff 16~30: 미지근하다고 출력하기
    elif 16 <= diff <= 30:
        print(f"미지근해요... (시도: {attempt}회)")
    # diff >= 31: 차갑다고 출력하기
    elif diff >= 31:
        print(f"차가워요! 멀리 있어요! (시도: {attempt}회)")

    # 이전 시도보다 diff가 작아졌으면 가까워진다고 출력하기
    if diff < prev_diff:
        print("점점 가까워지고 있어요!")
    prev_diff = diff