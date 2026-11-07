# input().split() 으로 두 칸을 나눠 각각 정수로 바꿉니다. 예: "3 3" → a=3, b=3
a, b = [int(x) for x in input().split()]

# 함수 정의하기
def is_equal(a, b):
    # 값 변환하기
    return a == b
# 결과 출력하기
print(is_equal(a,b))