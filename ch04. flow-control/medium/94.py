# 1부터 num까지 반복하며 나머지가 0이면 약수
num = int(input())
count = 0

# 1부터 num까지 반복하기
for i in range(1, num + 1):
    # 입력한 숫자가 i로 나누어 떨어지면 한 줄로 출력하기
    if num % i == 0:
        print(i)
        # 나누어 떨어지면 카운트 세기
        count += 1
# 총 약수 개수 출력하기
print("약수의 개수:", count)
