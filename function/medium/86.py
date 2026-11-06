# int(input()) 으로 정수 한 개를 읽습니다. 예: 입력이 "3661" 이면 sec == 3661
sec = int(input())

# 함수 정의하기
def to_hms(sec):
    # (시, 분, 초) 값 반환하기
    return (sec // 3600, (sec % 3600) // 60, sec % 60)
# 결과 출력하기
print(*to_hms(sec))