# for문으로 순회하며 '('와 ')'의 개수를 각각 세세요.
s = input()

# 괄호 여는 수 초기값 잡기
open_count = 0
# 괄호 닫는 수 초기값 잡기
close_count = 0

# 입력받은 문자열을 하나씩 살피기
for char in s:
    # 문자열 "(" 라면 열린 괄호 카운트 세기
    if char == "(":
        open_count += 1
    # 문자열 ")" 라면 닫힌 괄로 카운트
    elif char == ")":
        close_count += 1

# 만약 ( 수와 ) 수가 같으면 올바르다고 출력하기
if open_count == close_count:
    print("올바름")
# 그렇지 않으면 올바르지 않다고 출력하기
else:
    print("올바르지 않음")