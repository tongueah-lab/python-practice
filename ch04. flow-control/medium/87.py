# while True + break를 사용하세요.
total = 0
count = 0

# 숫자를 반복 입력받기
while True:
    num = int(input())
    # 입력한 숫자들을 누적 합하기
    total += num
    # 입력 횟수 세기
    count += 1
    # 만약 누적 합이 100이 넘는다면 초과했다고 알리고 총 누적 합, 총 입력횟수 출력하기
    if total > 100:
        print(f"누적합이 100을 초과했습니다!\n누적합: {total}\n입력 횟수: {count}")
        # 반복문 중단하기
        break
