# 전역 color = 첫 단어, inner = 둘째 단어. 예: "빨강 파랑" → color="빨강", inner="파랑"
parts = input().split()
color = parts[0]
inner = parts[1]

# 매개변수 없는 함수 정의하기
def paint():
    # 지역변수 두기
    color = inner
    # 값 반환하기
    return color
# 반환값 출력하기
print(paint())
# 전역 color 출력하기
print(color)