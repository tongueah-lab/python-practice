# 입력에서 width, height, fill 을 읽습니다. 예: "3 2 *" → width=3, height=2, fill="*"
parts = input().split()
width = int(parts[0])
height = int(parts[1])
fill = parts[2]

# 아래 함수는 이미 정의되어 있습니다 (수정하지 마세요).
def make_box(width, height, *, fill):
    return fill * (width * height)

# TODO: fill 은 키워드 전용이므로 make_box(width, height, fill=fill) 로 호출하고, 반환값을 print 하세요.
print(make_box(width, height, fill=fill))