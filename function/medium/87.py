# int(input()) 으로 정수 한 개를 읽습니다. 예: 입력이 "85" 이면 score == 85
score = int(input())

# 점수 검증 함수 정의하기
def evaluate(score):
    # 0~100 밖이면 "유효하지 않음" 값 반환하기
    if 0 > score or 100 < score:
        return "유효하지 않음"
    # 60 이상 "합격" 값 반환하기
    elif score >= 60:
        return "합격"
    # 미만 "불합격" 값 반환하기
    else:
        return "불합격"

# 점수 검증 출력하기
print(evaluate(score))