# for + if/elif/else + 카운팅 변수를 사용하세요.
positive = 0
negative = 0
zero = 0

# 합계는 0으로 잡기
total = 0

# 정수 10번 반복하기
for i in range(10):
    # 숫자 입력받기
    n = int(input())

    # 숫자가 0보다 큰 양수이면 카운트 하기
    if n > 0:
        positive += 1
    # 숫자가 0보다 작은 음수이면 카운트하기
    elif n < 0:
        negative += 1
    # 숫자가 0이면 카운트하기
    else:
        zero += 1
# 양수 총 개수 출력하기
print(f"양수: {positive}개")
# 음수 총 개수 출력하기
print(f"음수: {negative}개")
# 0 총 개수 출력하기
print(f"0: {zero}개")