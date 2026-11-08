# 문자열 text 를 입력에서 읽습니다. 예: "hi" → text="hi"
text = input()

# 문자열 함수 정의하기
def shout(s):
    # 매개변수 s에 "!"를 붙여 반환하기
    s = s + "!"
    return s

# 바뀐 문자열 출력하기
print(shout(text))
# 원본 출력하기
print(text)