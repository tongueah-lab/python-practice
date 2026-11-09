# 슬라이스 결과에 다시 `[::-1]` 을 체이닝하면 한 줄로 풀립니다.
data = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
a = int(input())
b = int(input())

# 데이터 a부터 b까지 슬라이스하기
result = data[a:b]
# 슬라이스 변수를 역순해서 출력하기
print(' '.join(map(str, result[::-1])))