# input().split() 으로 두 칸을 나눠 각각 정수로 바꿉니다. 예: "4 5" → w=4, h=5
w, h = [int(x) for x in input().split()]


# 둘레와 넓이 함수 정의하기
def rect(w, h):
    # 둘레, 넓이 값 반환하기
    return (2*(w+h), w*h)
# 결과 출력하기
print(*rect(w, h))