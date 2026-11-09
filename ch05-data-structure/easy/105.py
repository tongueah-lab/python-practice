# 문자열의 `count(sub)` 메서드는 sub이 몇 번 등장하는지 셉니다.
text = input()
target = input()

# 본문에 부분문자열이 몇 번 등장하는지 카운트세기
match_count = text.count(target)
# 결과 출력하기
print(match_count)