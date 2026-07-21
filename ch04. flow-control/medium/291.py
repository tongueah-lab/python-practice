# 등급별 카운터 5개를 두고 N번 반복하며 입력 점수에 맞는 카운터를 증가시키세요.
n = int(input())

# 등급 별로 점수 초기화하기
count_A = 0
count_B = 0
count_C = 0
count_D = 0
count_F = 0

# n번 반복하기
for _ in range(n):
    # 점수 입력받기
    score = int(input())
    # 90~100사이면 A 카운트하기
    if 90 <= score <= 100:
        count_A += 1
    # 80~89사이면 B 카운트하기
    elif 80 <= score <= 89:
        count_B += 1
    # 70~79사이면 C 카운트하기
    elif 70 <= score <= 79:
        count_C += 1
    # 60~69사이면 D 카운트하기
    elif 60 <= score <= 69:
        count_D += 1
    # 그 외면 F 카운트하기
    else:
        count_F += 1

# 등급 별로 몇 명인지 출력하기
print(f"A (90~100): {count_A}명")
print(f"B (80~89): {count_B}명")
print(f"C (70~79): {count_C}명")
print(f"D (60~69): {count_D}명")
print(f"F ( 0~59): {count_F}명")