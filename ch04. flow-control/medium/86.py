# for + if/elif/else + 카운팅 변수를 사용하세요.

# 카운트 변수 하나씩 잡기
a_count = 0
b_count = 0
c_count = 0
d_count = 0

# 10번 반복하기
for i in range(10):
    # 점수 입력받기
    score = int(input())
    # 90점 이상이면 카운트 세기
    if score >= 90:
        a_count += 1
    # 80점 이상이면 카운트 세기
    elif score >= 80:
        b_count += 1
    # 70점 이상이면 카운트 세기
    elif score >= 70:
        c_count += 1
    # 70점 미만이면 카운트 세기
    else:
        d_count += 1

# 점수마다 몇 명인지 출력하기
print(f"90점 이상: {a_count}명")
print(f"80점 이상: {b_count}명")
print(f"70점 이상: {c_count}명")
print(f"70점 미만: {d_count}명")