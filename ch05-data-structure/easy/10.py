# pop 의 반환값을 변수에 저장해두면 출력에 활용할 수 있습니다.
data_sets = [
    ["윤서", "지우", "민준", "서윤", "도윤"],
    ["A", "B", "C"],
    ["혼자"],
]
t = int(input())
applicants = data_sets[t]

# 취소 된 사람을 제거하고 그 값으 반환하기
canceled = applicants.pop()

# 취소된 사람 출력하기
print(f"취소된 사람: {canceled}")
# 남은 명단 출력하기
print(f"남은 명단: {' '.join(applicants)}")