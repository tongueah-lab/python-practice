# 문자열의 `endswith(suffix)` 메서드를 사용하세요.
text = input()
suffix = input()

# text가 suffix로 끝나면
if text.endswith(suffix):
    # yes 출력
    print("yes")
# 아니면
else:
    # no 출력
    print("no")