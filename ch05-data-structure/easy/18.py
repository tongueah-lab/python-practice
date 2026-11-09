# `lst[a:b]` 은 인덱스 a부터 b-1까지의 원소를 새 리스트로 반환합니다.
scores = [85, 92, 78, 95, 88, 70, 100, 65, 82, 90]
a = int(input())
b = int(input())

# 슬라이스 결과를 문자열로 변환 후 공백으로 연결하기
result = " ".join(map(str, scores[a:b]))

# a부터 b-1까지 추출하여 출력하기
print(result)