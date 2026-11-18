# 원본 dict 의 items() 를 순회하면서 if 절로 합격 조건을 검사하세요.
students = {"윤서": 85, "지우": 92, "민준": 65, "서윤": 78, "도윤": 95}
cutoff = int(input())

# 새 딕셔너리 만들기
result = {}
# 이름 점수 순회하기
for name, score in students.items():
    # 점수가 cutoff이상인 학생은
    if score >= cutoff:
        # 새딕셔너리에 저장하기
        result[name] = score

# 이름 점수 순회하기
for name, score in result.items():
    # 결과 출력하기
    print(f"{name}: {score}")