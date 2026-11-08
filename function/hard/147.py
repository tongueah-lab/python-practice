# 앞 두 토큰=단어 리스트 pair, 나머지 key=value=옵션 dict opts.
# 예: "hello world sep=_ end=?" → pair=["hello","world"], opts={"sep":"_","end":"?"}
tokens = input().split()
pair = tokens[:2]
opts = {}
for token in tokens[2:]:
    k, v = token.split("=")
    opts[k] = v

# 아래 함수는 이미 정의되어 있습니다 (수정하지 마세요).
def make(a, b, sep="-", end="!"):
    return a + sep + b + end

# TODO: make(*pair, **opts) 처럼 * 와 ** 를 함께 풀어 호출하고, 그 반환값을 print 하세요.
print(make(*pair, **opts))