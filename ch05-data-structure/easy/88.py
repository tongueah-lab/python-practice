# 빈 set은 `set()` 으로 만듭니다 (`{}` 는 빈 dict). `s.add(item)` 으로 추가.
n = int(input())

# 빈 set만들기
s = set()
# 입력 개수 N, 다음 N줄에 단어를 하나씩 입력받기
for _ in range(n):
    # set에 추가하기
    s.add(input())
# 정렬한 결과를 출력하기
print(*sorted(s))