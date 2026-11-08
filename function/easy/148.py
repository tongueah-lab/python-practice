# 첫 토큰=대표 메뉴, 나머지=사이드. 예: "비빔밥 김치 단무지" → name="비빔밥", sides=["김치","단무지"]
raw = input().split()
name = raw[0]
sides = raw[1:]

# 함수 정의하기
def menu(name, *sides):
    # 사이드가 있으면 "{name} (s1,s2,...)"
    if sides:
        return f"{name} ({','.join(sides)})"
    # 없으면 "{name}"
    else:
        return f"{name}"
# ↓ 호출부 (수정하지 마세요)
print(menu(name, *sides))
