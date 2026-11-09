# 빈 dict 의 길이는 0 입니다.
data_sets = [
    {"윤서": 85, "지우": 92, "민준": 65, "서윤": 78, "도윤": 95},
    {"A": 80, "B": 90, "C": 70},
    {},
]
t = int(input())
scores = data_sets[t]

# a라는 변수에 딕셔너리의 키 길이를 구하기
student_count = len(scores)
# 출력하기
print(f"총 {student_count}명")