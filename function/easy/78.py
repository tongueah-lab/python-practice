# input().split() 으로 두 칸을 나눠 각각 정수로 바꿉니다. 예: "17 5" → a=17, b=5
a, b = [int(x) for x in input().split()]

# 함수 정의하기
def divide(a, b):
    # 몫, 나머지 값 반환하기
    return a // b, a % b
# 결과 출력하기
print(*divide(a, b))