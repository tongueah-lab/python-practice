# for + if/elif를 사용하세요.
n = int(input())

# 학생 n명의 점수를 반복하기
for i in range(1, n + 1):
    # 점수 입력받기
    score = int(input())
    # 점수가 90점 이상이면 "90점 이상: ★★★★★" 결과
    if score >= 90:
        result = "★★★★★"
    # 점수가 80점 이상이면 "80점 이상: ★★★★" 결과
    elif score >= 80:
        result = "★★★★"
    # 점수가 70점 이상이면 "70점 이상: ★★★" 결과
    elif score >= 70:
        result = "★★★"
    # 점수가 60점 이상이면 "60점 이상: ★★" 결과
    elif score >= 60:
        result = "★★"
    # 그 외는 "60점 미만: ★" 결과
    else:
        result = "★"
    # "{i}번 학생: 별문자열"로 출력하기
    print(f"{i}번 학생: {result}")