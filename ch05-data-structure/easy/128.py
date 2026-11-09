# 카운터 변수를 두고 for 순회하며 cutoff 이상이면 +1 (또는 컴프리헨션 + len/sum 활용)
scores = [85, 92, 65, 78, 95]
cutoff = int(input())

# 카운트 초기화하기
count = 0

# 점수 리스트 순회하기
for score in scores:
    # 점수가 cutoff 이상이면 +1
    if score >= cutoff:
        count += 1

# 결과 출력하기
print(count)