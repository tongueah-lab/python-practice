# 위치 토큰: 첫째=first, 나머지=rest. "sep=값" 은 키워드 전용 구분자.
# 예: "x y z sep=+" → first="x", rest=["y","z"], sep="+"
raw = input().split()
pos = [t for t in raw if "=" not in t]
first = pos[0]
rest = pos[1:]
sep = "-"
for t in raw:
    if "=" in t:
        k, v = t.split("=", 1)
        if k == "sep":
            sep = v

# TODO: 여기에 함수 make_list(first, *rest, sep="-") 를 직접 정의(def)하세요. (아래 호출이 동작해야 함)

# 구분자로 함수 정의하기
def make_list(first, *rest, sep="-"):
    # sep로 이은 문자열 반환하기
    return sep.join([first] + list(rest))
# ↓ 호출부 (수정하지 마세요) — sep 은 키워드 전용이라 이름으로 전달
print(make_list(first, *rest, sep=sep))
