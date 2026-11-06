# 첫 토큰=base, 나머지 key=value=추가 항목(값은 정수). 예: "1000 a=100 b=200" → base=1000, extra={"a":100,"b":200}
raw = input().split()
base = int(raw[0])
extra = {}
for t in raw[1:]:
    k, v = t.split("=")
    extra[k] = int(v)

# 아래 함수는 이미 정의되어 있습니다 (수정하지 마세요).
def merge(base, **extra):
    total = base
    for k in extra:
        total += extra[k]
    return total

# TODO: extra 를 ** 로 풀어 merge(base, **extra) 로 호출하고, 반환값을 print 하세요.
print(merge(base, **extra))