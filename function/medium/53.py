# 정수 x 를 입력에서 읽습니다. 예: "10" → x=10
x = int(input())

# TODO: add_one(n) 을 정의하고, add_one(x) 반환값과 원본 x 를 두 줄로 print 하세요.
def add_one(n):
    # n + 1하기
    n = n + 1
    # 값 반환하기
    return n

# 반환 값 출력하기
print(add_one(x))
# 원본 값 출력하기
print(x)