# input().split() 으로 세 칸을 나눠 각각 정수로 바꿉니다. 예: "1 2 3" → a=1, b=2, c=3
a, b, c = [int(x) for x in input().split()]

# 함수 정의하기
def max_three(num1, num2, num3):
    # 내장 max()로 비교 로직 간소화
    return max(num1, num2, num3)
# 결과 출력하기
print(max_three(a, b, c))