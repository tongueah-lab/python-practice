# 문자열의 `startswith(prefix)` 메서드를 사용하세요.
text = input()
prefix = input()

# text가 prefix로 시작하면 startswith 사용: 시작 여부만 검사
if text.startswith(prefix):
    # yes 출력하기
    print("yes")
# 아니면
else:
    # no 출력하기
    print("no")