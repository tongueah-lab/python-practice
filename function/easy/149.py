# 첫 토큰=카테고리, 나머지=항목들. 예: "선호도 사과 바나나" → category="선호도", names=["사과","바나나"]
raw = input().split()
category = raw[0]
names = raw[1:]

# 순위 나열 함수 정의하기
def ranking(category, *names):
    # >로 이어붙여 항목 값 반환하기
    return f"{category}: {' > '.join(names)}"
# ↓ 호출부 (수정하지 마세요)
print(ranking(category, *names))
