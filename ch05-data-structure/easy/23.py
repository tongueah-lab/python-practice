# `lst[N:]` 으로 N번째 이후 원소를 한 번에 얻습니다.
data = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
n = int(input())

# 정수로 변환 후 data 리스트를 n부터 슬라이싱 하기
result = " ".join(map(str, data[n:]))
# 출력하기
print(result)