# 입력에서 name, level 을 읽습니다. 예: "title 3" → name="title", level=3
parts = input().split()
name = parts[0]
level = int(parts[1])

# 아래 함수는 이미 정의되어 있습니다 (수정하지 마세요).
def tag(name, *, level):
    return "#" * level + name

# TODO: level 은 키워드 전용이므로 tag(name, level=level) 로 호출하고, 반환값을 print 하세요.
print(tag(name, level=level))