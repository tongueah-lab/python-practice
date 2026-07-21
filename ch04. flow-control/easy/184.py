# N개의 숫자를 입력받아 양수 합, 음수 합, 전체 합을 출력하세요.
n = int(input())

# 양수 합, 음수 합 초기화하기
positive_sum = 0
negative_sum = 0

# n개의 숫자 반복하기
for i in range(n):
    # 숫자들 입력받기
    nums = int(input())
    # 숫자가 양수이면 더하기
    if nums > 0:
        positive_sum += nums
    
    # 숫자가 음수이면 더하기
    elif nums < 0:
        negative_sum += nums
    
# 전체 더하기
total_sum = positive_sum + negative_sum

# 양수, 음수, 전체 합 출력하기
print(f"양수 합: {positive_sum}")
print(f"음수 합: {negative_sum}")
print(f"전체 합: {total_sum}")