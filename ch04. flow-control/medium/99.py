# 모드에 따라 변환 공식을 선택하고 최고/최저 갱신
mode = int(input())
n = int(input())
max_temp = -9999
min_temp = 9999

# 개수만큼 반복하기
for i in range(n):

    # 모드가 1이면 섭씨 -> 화씨
    if mode == 1:
        # 섭씨 온도 입력받기
        C = float(input())
        converted = C * 9 / 5 + 32
        print(f"변환 결과: {converted}°F")

    # 모드가 2이면 화씨 -> 섭씨
    elif mode == 2:
        # 화씨 온도 입력받기
        F = float(input())
        converted = (F - 32) * 5 / 9
        print(f"변환 결과: {converted}°C")

    # 최고 온도보다 섭씨가 더 크면
    if max_temp < converted:
        # 변환된 섭씨 온도 중 제일 최고 온도로 저장됨
        max_temp = converted

    # 최저 온도보다 섭씨가 작으면
    if min_temp > converted:
        # 변환된 섭씨 온도 중 제일 최저 온도로 저장됨
        min_temp = converted

# 최고,최저 온도 출력하기        
print("최고 변환 온도:", max_temp)
print("최저 변환 온도:", min_temp)