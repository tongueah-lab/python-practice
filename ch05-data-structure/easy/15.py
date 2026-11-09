# 합과 개수로 평균을 구하고 소수점 첫째 자리 포맷으로 출력하세요.
data_sets = [
    [85, 92, 78, 95, 88, 70, 100, 65, 82, 90],
    [50, 60, 70],
    [100],
]
t = int(input())
scores = data_sets[t]

# 점수 총합 구하기
total = sum(scores)
# 총합 출력하기
print(f"총합: {total}")

# 평균 구하기
avg = total / len(scores)
# 평균 출력하기
print(f"평균: {avg:.1f}")