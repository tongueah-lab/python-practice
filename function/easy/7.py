# input().split() 으로 두 칸을 나눠 각각 정수로 바꿉니다. 예: "3 4" → a=3, b=4
num1, num2 = [int(x) for x in input().split()]

# 함수 정의하기
def multiply(num1, num2):
    # 두 수의 곱으로 값 반환하기
    return num1 * num2
# 두 수의 곱 출력하기
print(multiply(num1, num2))