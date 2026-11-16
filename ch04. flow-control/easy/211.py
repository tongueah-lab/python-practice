# for문으로 한 글자씩 생성하세요.
n = int(input())

# 알파벳 a부터 시작 변수
alpha = "a"
# 숫자 1부터 시작 변수
num = 1

# 알파벳은 a부터 순서대로
for i in range(1, n + 1):
    # 홀수 번째 자리이면 알파벳
    if i % 2 == 1:
        # 알파벳 줄 바꿈 없이 출력
        print(alpha, end = "")
        # 알파벳 하나씩 증가하기
        alpha = chr(ord(alpha) + 1)
        # 알파벳이 z를 넘으면 a로 돌아감
        if alpha > "z":
            alpha = "a"

    # 짝수 번째 자리이면 숫자
    else:
        # 숫자 줄 바꿈없이 출력하기
        print(num, end = "")
        # 숫자 1씩 증가하기
        num += 1
        # 숫자가 9를 넘으면 0으로 돌아감
        if num > 9:
            num = 0