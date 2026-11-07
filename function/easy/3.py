# input().split() 으로 두 칸을 나눠 각각 정수로 바꿉니다. 예: "10 2" → a=10, b=2
a, b = [int(x) for x in input().split()]

# 함수 정의하기
def bigger(a, b):
    
    # return으로 값 반환하기
    if a >= b:
        return a
    else:
        return b
# 결과 출력하기
print(bigger(a, b))