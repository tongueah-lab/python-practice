# 절대값은 if로 직접 계산하세요. chance 변수로 시도 횟수 추적
answer = 7
max_chance = 3


chance = 0

# 행운의 룰렛 출력하기
print("=== 행운의 룰렛 ===")
print("1~10 중 숫자를 맞춰보세요! (기회: 3번)")
print()
# 참이 될 때까지 반복하기
while True:
    
    # 숫자 입력받기
    num = int(input())
    # 만약 정답이면 정답이라고 출력 후 종료
    if num == answer:
        print("정답입니다! 축하합니다!")
        break
    # 차이가 1이면 가깝다고 출력 하기
    elif abs(num - answer) == 1:
        chance += 1
        print(f"아주 가까워요! (뜨거워!) (남은 기회: {max_chance - chance}번)")
        

    # 차이가 2~3이면 가깝다고 출력 하기
    elif 2 <= abs(num - answer) <= 3:
        chance += 1
        print(f"가까워요! (따뜻해요) (남은 기회: {max_chance - chance}번)")
    
    # 차이가 4 이상이면 멀다고 출력하기
    elif abs(num - answer) >= 4:
        chance += 1
        print(f"멀어요... (차가워요) (남은 기회: {max_chance - chance}번)")
    

    # 기회를 다 쓰면 다 썼다고 출력 후 반복문 종료하기
    if chance == max_chance:
        print("기회를 모두 사용했습니다. 정답은 7이었습니다.")
        break