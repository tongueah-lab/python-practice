# 1부터 num-1까지의 약수의 합을 구해 비교
num = int(input())
total = 0

# 1부터 num - 1까지 반복하기
for i in range(1, num):
    # 입력받은 숫자가 i에 나누어 떨어지면 약수
    if num % i == 0:
        # 약수들의 합
        total += i

# 약수의 합 출력하기
print(f"{num}의 약수의 합: {total}")

# 합이 자기 자신과 같으면 완전수라고 출력하기
if total == num:
    print(f"{num}은(는) 완전수입니다!")
# 합이 자기 자신과 다르면 완전수가 아니라고 출력하기
else:
    print(f"{num}은(는) 완전수가 아닙니다.")