# dict는 `d[key]` 로 값을 조회합니다.
scores = {"윤서": 85, "지우": 92, "민준": 65, "서윤": 78, "도윤": 95}
name = input()

# 학생 이름으로 점수 찾아서 출력하기
# print(scores[name])


score = scores.get(name)
if score is not None:
    print(score)