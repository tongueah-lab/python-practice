# input().split() 으로 두 칸을 나눠 각각 정수로 바꿉니다. 예: "4 5" → w=4, h=5
w, h = [int(x) for x in input().split()]

# 직사각형 넓이 정의하기
def area(w, h):
    # 가로 w와 세로 h를 받아 w * h로 넓이를 구해 반환하기
    return w * h
# 결과 출력하기
print(area(w, h))