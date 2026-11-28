# 각 그룹 list 를 빌딩 후 빈 경우 라벨만 출력.
s1_sets = [
    {"윤서": 85, "지우": 92, "민준": 65},
    {"A": 80, "B": 90, "C": 70},
    {"X": 50},
]
s2_sets = [
    {"지우": 88, "민준": 70, "도윤": 95, "예준": 60},
    {"A": 85, "B": 95, "C": 75},
    {"Y": 60},
]
t = int(input())
s1 = s1_sets[t]
s2 = s2_sets[t]

# 1학기에만 있는 학생 리스트
only1 = []
# 2학기에만 있는 학생 리스트
only2 = []
# 둘 다 있는 학생 리스트
both = []

# 1학기 순회하기
for name in s1:
    # 만약 2학기 학생이 없으면
    if name not in s2:
        # 1학기 학생 리스트에 추가하기
        only1.append(name)
    # 2학기 학생도 있으면
    else:
        # 둘 다 있는 리스트에 추가하기
        both.append(name)
# 2학기 순회하기
for name in s2:
    # 1학기 학생이 없으면 
    if name not in s1:
        # 2학기 학생 리스트에 추가하기
        only2.append(name)
# 1학기만 출력하기
if only1:
    print("1학기만:", " ".join(only1))
else:
    print("1학기만:")
# 2학기만 출력하기
if only2:
    print("2학기만:", " ".join(only2))
else:
    print("2학기만:")
# 양학기 출력하기
if both:
    print("양학기:", " ".join(both))
else:
    print("양학기:")