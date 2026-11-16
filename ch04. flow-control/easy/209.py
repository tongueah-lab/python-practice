# N을 입력받아 1~N*N 숫자를 N열씩 탭 구분으로 출력하세요.
n = int(input())

# 변수 1로 초기화하기
num = 1
# 정수 n을 n번 반복하기
for i in range(1, n + 1):
    # 가로로 n번 반복하기
    for j in range(1, n + 1):
        # 1씩 반복하기
        print(num, end = "\t")
        num += 1
    # 결과 출력하기
    print()