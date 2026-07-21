# for i in range(5): num = int(input()); if num % 2 != 0: print("홀수는 건너뜁니다"); continue; total += num
total = 0

# 정수 5개를 입력받는다
for i in range(5):
    num = int(input())
    # 정수가 홀수이면 건너뛰고 계속한다
    if num % 2 != 0:
        print("홀수는 건너뜁니다")
        continue
    # 홀수가 아니면 값들을 누적 합 한다
    total += num
# 짝수 합계 출력하기
print("짝수 합계:", total)