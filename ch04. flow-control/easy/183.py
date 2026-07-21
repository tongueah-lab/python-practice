# 가로와 세로를 입력받아 별(*) 사각형을 출력하세요.
width = int(input())
height = int(input())

# 세로로 반복 출력하기
for i in range(1, height + 1):
    # 가로로 반복 출력하기
    for j in range(1, width + 1):
        # *을 한 줄로 출력하기
        print("*", end="")
    # 반복 끝나면 한 줄씩 띄우기
    print()