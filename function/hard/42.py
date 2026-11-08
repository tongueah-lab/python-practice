# 전역 count = 첫 값, step = 둘째 값. 예: "100 5" → count=100, step=5
parts = input().split()
count = int(parts[0])
step = int(parts[1])


# 지역변수의 생명주기 함수 정의하기
def bump():
    # 지역변수
    count = step
    # 그 값을 반환하기
    return count
# 결과 출력하기
print(bump())
print(bump())
print(count)