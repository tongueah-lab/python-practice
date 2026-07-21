# 도형 종류에 따라 필요한 값을 입력받으세요.
shape = input()

# 도형이 원이면
if shape == "원":
    # 반지름 입력받기
    radius = int(input())
    # 원의 넓이 = 반지름 * 반지름 * 3.14
    area = radius * radius * 3.14
    # 소수점 둘째 자리까지 출력하기
    print(f"넓이: {area:.2f}")

# 도형이 삼각형이면
elif shape == "삼각형":
    # 밑변, 높이 입력받기
    bottom = int(input())
    height = int(input())
    # 삼각형의 넓이 = 밑변 * 높이 / 2
    area = bottom * height / 2
    # 소수점 첫째 자리까지 출력하기
    print(f"넓이: {area:.1f}")

# 도형이 사각형이면
elif shape == "사각형":
    # 가로, 세로 입력받기
    length = int(input())
    width = int(input())
    # 사각형의 넓이 = 가로 * 세로
    area = length * width
    # 정수로 출력하기
    print(f"넓이: {area}")