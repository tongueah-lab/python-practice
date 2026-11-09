# 끝 N개를 자르는 것은 음수 인덱스 슬라이싱 `lst[:-N]` 으로 가능합니다.
data = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
n = int(input())

# 정수로 변환 후 음수 인덱스 슬라이싱 하기
result = " ".join(map(str, data[:-n]))

# 출력하기
print(result)