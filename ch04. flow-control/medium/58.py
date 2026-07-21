# 바깥 for문으로 줄, 안쪽 for문으로 별 개수를 제어하세요.
n = int(input())

# 가로로 한 줄씩 받기
for col in range(1):
    # 세로로 1부터 n까지 줄 번호 순회하기
    for row in range(1, n + 1):
        # 해당 줄 번호만큼 별을 출력하기
        print("*" * row)
        