# 정렬이 아니라 단순 역순임에 유의.
data_sets = [
    ["윤서", "지우", "민준", "서윤", "도윤", "예준"],
    ["red", "green", "blue"],
    ["혼자"],
]
t = int(input())
names = data_sets[t]

# 슬라이싱으로 역순 리스트를 만든 후 공백으로 구분하기
result = " ".join(names[::-1])

# 출력하기
print(result)