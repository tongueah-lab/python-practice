# step 인자에 -1을 주어 역순 사본을 만듭니다.
data_sets = [
    [85, 92, 78, 95, 88, 70, 100, 65, 82, 90],
    [1, 2, 3],
    [42],
]
t = int(input())
scores = data_sets[t]

# 역순으로 슬라이싱 만들기
# scores[::-1]은 원본 리스트를 변경하지 않고 역순 사본을 생성함
result = " ".join(map(str, scores[::-1]))

# 출력하기
print(result)