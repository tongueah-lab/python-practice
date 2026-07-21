# for문으로 문자열을 순회하며 플래그를 사용하세요.
s = input()

# 아직 @를 찾지 못한 상태
has_at = False
# 아직 .을 찾지 못한 상태
has_dot = False

# 한 글자씩 반복하기
for ch in s:
    # ch가 @이면 찾음
    if ch == "@":
        has_at = True

    # ch가 .이면 찾음
    if ch == ".":
        has_dot = True

    # 두 개가 다 있으면 더 반복할 필요 없음
    if has_at and has_dot:
        break

# has_at과 has_dot이 모두 포함되어 있으면 유효 출력하기
if has_at and has_dot:
    print("유효")
# 하나라도 없으면 무효 출력하기
else:
    print("무효")