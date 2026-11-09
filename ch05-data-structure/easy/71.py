# `d.get(key, 기본값)` 은 키가 없을 때 KeyError 대신 기본값을 반환합니다.
scores = {"윤서": 85, "지우": 92, "민준": 65, "서윤": 78, "도윤": 95}
name = input()

# 점수를 조회하되 없는 학생이면 0을 출력하기
print(scores.get(name, 0))