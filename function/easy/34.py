# 전역변수 word 를 입력에서 읽습니다. 예: "hello" → word="hello"
word = input()

# 함수 정의하기
def count():
    # 전역 + 내장 값 반환하기
    return len(word)
# 결과 출력하기
print(count())