# 입력에서 text, start, end 를 읽습니다. 예: "hello 1 4" → text="hello", start=1, end=4
parts = input().split()
text = parts[0]
start = int(parts[1])
end = int(parts[2])

# 아래 함수는 이미 정의되어 있습니다 (수정하지 마세요).
def slice_text(text, *, start, end):
    return text[start:end]

# TODO: start, end 는 키워드 전용이므로 slice_text(text, start=start, end=end) 로 호출하고 print 하세요.
print(slice_text(text, start=start, end=end))