# for + if + 카운팅 변수를 사용하세요.
n = int(input())

# 개수 초기화하기
count = 0
# 1부터 n까지 반복하기
for i in range(1, n + 1):
    # 만약 2로 나누어떨어지는 짝수이면 개수 세기
    if i % 2 == 0:
        count += 1
# 짝수 개수 출력하기
print(f"1부터 {n}까지 짝수의 개수: {count}")