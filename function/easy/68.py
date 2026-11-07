# int(input()) 으로 정수 한 개를 읽습니다. 예: 입력이 "95" 이면 score == 95
score = int(input())

# 점수 함수 정의하기
def grade(score):
    # 90이상이면 A
    if score >= 90:
        return "A"
    # 80이상 90미만이면 B
    elif 80 <= score < 90:
        return "B"
    # 70이상 80미만이면 C
    elif 70 <= score < 80:
        return "C"
    # 70미만이면 F
    else:
        return "F"
# 결과 출력하기
print(grade(score))