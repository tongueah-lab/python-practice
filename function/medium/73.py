# int(input()) 으로 정수 한 개를 읽습니다. 예: 입력이 "130" 이면 sec == 130
sec = int(input())

# 초를 분,초 문자열로 함수 정의하기
def sec_to_str(sec):
    # 반환하기
    return f"{sec // 60}분 {sec % 60}초"
# 결과 출력하기
print(sec_to_str(sec))