# 바깥 if는 파일명, 안쪽 if는 확장자 기준으로 작성하세요.
filename = input()
extension = input()

# 파일명이 있으면,
if filename:
    # 확장자가 txt이면 텍스트 파일 저장 출력하기
    if extension == "txt":
        print("텍스트 파일 저장")
    # 아니면 지원되지 않는 형식이라고 출력하기
    else:
        print("지원되지 않는 형식")
# 파일명이 빈 문자열이면 파일명 입력하라고 출력하기
else:
    print("파일명을 입력하세요")