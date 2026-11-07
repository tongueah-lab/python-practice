# int(input()) 으로 정수 한 개를 읽습니다. 예: 입력이 "1" 이면 m == 1
m = int(input())

# 분을 초로 변환하는 함수 정의하기
def to_seconds(m):
    # 입력받은 분에 60을 곱해서 초로 값 변환하기
    return m * 60
# 결과 출력하기
print(to_seconds(m))