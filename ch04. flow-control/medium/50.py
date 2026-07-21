# while True 안에서 정답일 때 break 하세요.
answer = 42

# 반복하고 입력받기
while True:
    number = int(input())
    # 입력한 수가 정답이면 "정답입니다!" 출력하고 멈추기
    if number == answer:
        print("정답입니다!")
        break
    # 입력한 수가 정답보다 작으면 "더 큰 수를 입력하세요" 출력하기
    elif number < answer:
        print("더 큰 수를 입력하세요")
    # 그 외는 "더 작은 수를 입력하세요" 출력하기
    else:
        print("더 작은 수를 입력하세요")