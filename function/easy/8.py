# input().split() 으로 세 칸을 나눠 각각 정수로 바꿉니다. 예: "1 2 3" → a=1, b=2, c=3
a, b, c = [int(x) for x in input().split()]

# 세 수의 합 함수 정의하기
def sum_three(a, b, c):
    # 세 수의 합 값 반환하기
    return a + b + c
# 세 수의 합 결과 출력하기
print(sum_three(a, b, c))