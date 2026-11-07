# 전역 count 시작값 0. 호출 횟수 n 을 입력에서 읽습니다. 예: "5" → n=5
count = 0
n = int(input())


# 카운터 증가 함수 정의하기
def increase():
    # global 선언 후
    global count
    # 1씩 늘리는 값 반환하기
    count += 1
# n번 호출 후
for _ in range(n):
    increase()
# 결과 출력하기
print(count)