# 각 학생 점수 입력 후 target 점수를 고르고 더 높은 수 세기
print("=== 5명의 점수 입력 ===")
s1 = int(input())
s2 = int(input())
s3 = int(input())
s4 = int(input())
s5 = int(input())
target = int(input())

# 석차 순서잡기1
result = 1

# 타겟이 1이면 점수는 s1
if target == 1:
    score = s1
# 타겟이 2이면 점수는 s2
elif target == 2:
    score = s2
# 타겟이 3이면 점수는 s3
elif target == 3:
    score = s3
# 타겟이 4이면 점수는 s4
elif target == 4:
    score = s4
# 타겟이 5이면 점수는 s5
elif target == 5:
    score = s5

# 점수가 s1보다 작으면 석차 +1
if score < s1:
    result += 1
# 점수가 s2보다 작으면 석차 +1
if score < s2:
    result += 1
# 점수가 s3보다 작으면 석차 +1
if score < s3:
    result += 1
# 점수가 s4보다 작으면 석차 +1
if score < s4:
    result += 1
# 점수가 s5보다 작으면 석차 +1
if score < s5:
    result += 1


# 입력받은 학생 점수 출력하기
print(f"{target}번 학생 점수: {score}")
# 석차 출력하기
print(f"석차: {result}등")