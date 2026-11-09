# 항목 삭제는 `del d[key]` 또는 `d.pop(key)` 로 가능합니다.
scores = {"윤서": 85, "지우": 92, "민준": 65, "서윤": 78, "도윤": 95}
name = input()

# 점수 리스트에 있는 이름 삭제하기
del scores[name]

# 결과 출력하기
for student, score in scores.items():
    print(f"{student}: {score}")