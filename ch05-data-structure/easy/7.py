# 리스트에 같은 값이 몇 개인지 셀 때는 count 메서드가 편리합니다.
scores = [85, 92, 78, 85, 88, 85, 100, 65, 82, 90]
target_score = int(input())

# 카운트 초기화하기
count = 0

# 점수 리스트 반복하기
for score in scores:
    # 리스트에 같은 값이 있으면 카운트 세기
    if score == target_score:
        # 카운트 세기
        count += 1
# 카운트 출력하기
print(count)