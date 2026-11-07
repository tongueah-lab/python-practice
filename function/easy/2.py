# input().split() 으로 두 칸을 나눠 각각 정수로 바꿉니다. 예: "3 5" → a=3, b=5
num1, num2 = [int(x) for x in input().split()]

# 두 수의 합을 반환하는 함수 정의하기
def add(num1, num2):
    # return으로 값 반환하기
    return num1 + num2
# 결과 출력하기
print(add(num1, num2))