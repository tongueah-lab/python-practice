# strict greater (>) 비교로 첫 본 학생을 유지.
data_sets = [
    {"윤서": 85, "지우": 92, "민준": 65, "서윤": 78, "도윤": 95},
    {"A": 80, "B": 90, "C": 70},
    {"혼자": 100},
]
t = int(input())
scores = data_sets[t]

# 초기값 잡기
top_name, top_score = "", -1

# 이름 점수 순회하기
for name, score in scores.items():
    # 입력한 번호가 최고 점수보다 크면
    if score > top_score:
        # 최고 학생으로 등록하기
        top_name = name
        # 최고 점수로 등록하기
        top_score = score

# 이름: 점수 출력하기
print(f"{top_name}: {top_score}")