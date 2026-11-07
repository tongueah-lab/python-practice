# int(input()) 으로 정수 한 개를 읽습니다. 예: 입력이 "5" 이면 s == 5
s = int(input())

# 정사각형 한 변의 길이를 함수로 정의하기
def square_area(s):
    # 한 변의 길이 s를 받아 넓이(s * s)를 반환한다
    return s * s
# 결과 출력하기
print(square_area(s))