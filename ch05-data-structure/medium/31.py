# 앞쪽 K개 제거(`K:`)와 뒤쪽 K개 제거(`:-K`)를 한 슬라이스에 모두 적용하세요.
# 단, K=0 인 경우 `data[0:-0]` 은 빈 슬라이스가 되므로 따로 처리하거나 다른 형태를 써야 합니다.
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
k = int(input())

# k가 0이면 데이터 그대로
if k == 0:
    result = data
# 0이 아니면 앞쪽 k부터 뒤쪽 k까지
else:
    result = data[k:-k]

# 결과 출력하기
print(' '.join(map(str, result)))