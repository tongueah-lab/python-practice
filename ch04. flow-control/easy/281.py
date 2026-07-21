# 끝값은 포함되지 않는 점에 유의해 for 반복문을 작성하세요.
start = int(input())
stop = int(input())
step = int(input())

# 시작값, 끝 값, 간격 순으로 반복 순회하기
for i in range(start, stop, step):
    # end=" "로 공백 구분, 줄바꿈 없이 이어 출력
    print(i, end=" ")