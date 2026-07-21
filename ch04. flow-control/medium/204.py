# 콜라츠 추측 과정과 횟수를 출력하세요.
n = int(input())

# 카운트 초기화 하기
count = 0
# 입력 값 출력하기
print(n)

# 반복문 실행하기
while True:

    # 만약 숫자가 1이 되면 반복문 중단하고 카운트 세기
    if n == 1:
        break
        count += 1

    # 짝수면 2로 나누고 카운트 세고 나온 값으로 반복하기
    elif n % 2 == 0:
        result = n / 2
        n = result
        print(int(n))
        count += 1

    # 홀수면 3을 곱하고 1을 더하고 카운트 세고 나온 값으로 반복하기
    else:
        result = (n * 3) + 1
        n = result
        print(int(n))
        count += 1
    
# 반복한 횟수 출력하기
print(f"횟수: {count}")