# 두 평균 비교 후 셋 중 하나 출력.
s1_sets = [
    {"윤서": 85, "지우": 92, "민준": 65},
    {"A": 90, "B": 90},
    {"X": 80, "Y": 80},
]
s2_sets = [
    {"지우": 88, "민준": 70, "도윤": 95},
    {"C": 70, "D": 80},
    {"P": 80, "Q": 80},
]
t = int(input())
s1 = s1_sets[t]
s2 = s2_sets[t]

# 1학기 평균 출력하기
semester1_avg = sum(s1.values()) / len(s1)
print(f"1학기 평균: {semester1_avg:.1f}")

# 2학기 평균 출력하기
semester2_avg = sum(s2.values()) / len(s2)
print(f"2학기 평균: {semester2_avg:.1f}")

# 평균이 1학기가 더 높다면
if semester1_avg > semester2_avg:
    # 승리는 1학기
    result = "1학기"
# 평균이 2학기가 더 높다면
elif semester1_avg < semester2_avg:
    # 승리는 2학기
    result = "2학기"
# 동률이면
else:
    # 무승부
    result = "무승부"
# 결과 출력하기
print(f"승: {result}")