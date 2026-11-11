# `scores.values()` 를 순회하며 cutoff 이상인 값의 개수를 세세요.
scores = {"윤서": 85, "지우": 92, "민준": 65, "서윤": 78, "도윤": 95}
cutoff = int(input())

# 학생 수 초기화하기
student_count = 0
# scores안의 점수 값을 살펴보기
for score in scores.values():
    # 점수가 cutoff 이상이면
    if score >= cutoff:
        # 학생 수 더하기
        student_count += 1
# 결과 출력하기
print(student_count)