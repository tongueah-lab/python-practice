# input() 으로 문자열 한 줄을 읽습니다. 예: 입력이 "hello" 이면 s == "hello"
s = input()

# 문자열 뒤집기 함수 정의하기
def reverse(s):
    # 슬라이싱을 사용하여 값 반환하기
    return s[::-1]
# 문자열 뒤집기 출력하기
print(reverse(s))