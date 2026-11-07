# input().split() 으로 두 칸을 나눠 각각 정수로 바꿉니다. 예: "10 2" → a=10, b=2
a, b = [int(x) for x in input().split()]

# 안전한 나눗셈 함수 정의하기
def safe_divide(a, b):
    # b == 0이면 "오류"로 값 반환하기
    if b == 0:
        return "오류"
    # 아니면 a // b로 값 반환하기
    return a // b
# 반환값 한 줄로 출력하기
print(safe_divide(a, b))