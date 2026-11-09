# `target in text` 로 먼저 검사하고, 있으면 `text.index(target)` 으로 위치를 구하세요.
text = input()
target = input()

# text안에 target을 검사하고 있으면
if target in text:
    # 위치 구하기
    print(text.index(target))
# 없으면
else:
    # 없음 출력하기
    print("없음")