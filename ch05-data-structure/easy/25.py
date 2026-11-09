# 음수 인덱스도 슬라이스의 양 끝에 사용 가능합니다 — 끝에서부터의 위치를 의미합니다.
data = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
a = int(input())
b = int(input())

# 정수로 변환 후 음수 슬라이싱 하기
result = " ".join(map(str, data[a:b]))
# 출력하기
print(result)