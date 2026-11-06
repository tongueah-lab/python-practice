# input() 으로 문자열 한 줄을 읽습니다. 예: 입력이 "racecar" 이면 s == "racecar"
s = input()

# 함수 정의하기
def is_palindrome(s):
    # 거꾸로 있어도 똑같은 회문이면 "True"
    if s == s[::-1]:
        return "True"
    # 아니면 "False"
    else:
        return "False"
# 회문 판별 함수 결과 출력하기
print(is_palindrome(s))