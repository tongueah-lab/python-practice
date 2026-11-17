# `for name, s in scores.items():` 순회하며 조건 만족하는 이름을 모으세요.
scores = {"윤서": 85, "지우": 92, "민준": 65, "서윤": 78, "도윤": 95}
cutoff = int(input())

# 이름 저장할 곳
names = []
# 이름, 점수 순회하기
for name, s in scores.items():
    # 점수가 cutoff 이상이면
    if s >= cutoff:
        # 이름 저장하기
        names.append(name)
# 결과 출력하기
print(" ".join(names))