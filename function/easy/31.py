# 전역변수 message 를 입력에서 읽습니다. 예: "회의 3시" → message="회의 3시"
message = input()

# 함수 정의하기
def announce():
    # 매 [공지]와 함께 메시지로 값 반환하기
    return "[공지] " + message
# 결과 출력하기
print(announce())