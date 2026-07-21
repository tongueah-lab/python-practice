# for i in range(1, 21): if i % 3 == 0: continue; print(i)

# 1 부터 20까지 반복하기
for i in range(1, 21):
    # 만약 3으로 나누어 떨어지면 건너뛰기
    if i % 3 == 0:
        continue
    # 출력하기
    print(i)