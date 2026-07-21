# for + if를 사용하세요.
n = int(input())
count = 0

# 학생수 n명 입력받기
for i in range(n):
    # 학생 점수 입력받기
    score = int(input())
    # 60점 이상인 합격자 수 세기
    if score >= 60:
        count += 1
# 총 합격자 수 출력하기
print("합격자 수:", count)
