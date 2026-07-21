# 10번 반복하며 양수/음수/0 분류
pos_sum = 0
neg_sum = 0
zero_count = 0

# 10개의 숫자를 반복하기
for i in range(10):
    # 하나씩 입력받기
    number = int(input())
    # 만약 입력받은 숫자가 0보다 큰 양수이면 다 합하기
    if number > 0:
        pos_sum += number
    # 입력받은 숫자가 0보다 작은 음수이면 다 합하기
    elif number < 0:
        neg_sum += number
    # 그 외 0이면 개수 세기
    else:
        zero_count += 1
        
print("양수의 합:", pos_sum)
print("음수의 합:", neg_sum)
print("0의 개수:", zero_count)
