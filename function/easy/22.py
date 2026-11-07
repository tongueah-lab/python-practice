# 입력에서 text, times 를 읽습니다. 예: "ab 3" → text="ab", times=3
parts = input().split()
text = parts[0]
times = int(parts[1])

# 아래 함수는 이미 정의되어 있습니다 (수정하지 마세요).
def repeat(text, *, times):
    return text * times

# TODO: times 는 키워드 전용이므로 repeat(text, times=times) 로 호출하고, 반환값을 print 하세요.

print(repeat(text, times=times))