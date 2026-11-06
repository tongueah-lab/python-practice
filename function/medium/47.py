# 전역 status 시작값 "대기". 설정할 상태들을 순서대로 읽습니다. 예: "진행 완료" → commands=["진행","완료"]
status = "대기"
commands = input().split()


# 문자열 함수 정의하기
def set_status(new):
    # global 선언하기
    global status
    status = new

# 모든 상태를 순서대로 설정하기
for command in commands:
    set_status(command)

# 결과 출력하기
print(status)