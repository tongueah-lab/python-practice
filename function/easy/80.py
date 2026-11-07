# input().split() 으로 두 칸을 나눠 각각 정수로 바꿉니다. 예: "3 5" → a=3, b=5
a, b = [int(x) for x in input().split()]


# 합과 곱 함수 정의하기
def sum_product(a, b):
    # 합, 곱 값 반환하기
    return a + b, a * b
# 결과 출력하기
print(*sum_product(a, b))