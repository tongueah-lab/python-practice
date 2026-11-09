# `sub in text` 형태로 부분문자열 존재 여부를 확인할 수 있습니다 (위치는 모름).
text = input()
sub = input()

# 본문에 부분문자열이 포함되어 있으면
if sub in text:
    # 포함 출력하기
    print("포함")
# 없으면
else:
    # 미포함 출력하기
    print("미포함")