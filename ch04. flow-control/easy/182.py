# N을 입력받아 1~N에서 3의 배수, 5의 배수, 공배수 개수를 세어 출력하세요.
n = int(input())

# 카운트들의 초기화하기
a_count_of_3 = 0
b_count_of_5 = 0
c_count_of_15 = 0

# 1부터 n까지 반복하기
for i in range(1, n + 1):
    # 3으로 나누어 떨어지는 3의 배수이면 개수 세기
    if i % 3 == 0:
        a_count_of_3 += 1
    # 5로 나누어 떨어지는 5의 배수이면 개수 세기
    if i % 5 == 0:
        b_count_of_5 += 1
    # 3과 5로 똑같이 나누어 떨어지는 공배수 개수 세기
    if i % 15 == 0:
        c_count_of_15 += 1

# 3의 배수 개수 출력하기
print(f"3의 배수: {a_count_of_3}개")
# 5의 배수 개수 출력하기
print(f"5의 배수: {b_count_of_5}개")
# 3과 5의 공배수 개수 출력하기
print(f"3과 5의 공배수: {c_count_of_15}개")