# input().split() 으로 두 칸을 나눕니다. 예: "김 철수" → last="김", first="철수"
last, first = input().split()

# 성과 이름 분리 함수 정의하기
def name_order(last, first):
    # (이름, 성) 순서로 함께 반환하기
    return (first, last)
# 이름 성 형식으로 출력하기
print(*name_order(last, first))