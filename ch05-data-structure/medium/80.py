# `students[name]` 자체가 점수 리스트 입니다. sum() 과 len() 으로 평균을 구하세요.
students = {
    "윤서": [85, 90, 78],
    "지우": [92, 88, 95],
    "민준": [65, 70],
    "서윤": [80, 80, 80, 80],
}
name = input()

# 점수만 가져오기
score = students[name]
# 평균 구하기
avg = sum(score) / len(score)
# 결과 출력하기
print(f"평균: {avg:.1f}")