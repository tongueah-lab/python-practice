# max_val = -1로 초기화하고, 입력을 받아가며 현재 값이 더 크면 갱신하세요.

max_val = -1

# 반복문 실행하기
while True:
    # num 입력받기
    num = int(input())
    # 만약 num이 -1이면 반복 중단하기
    if num == -1:
        break
    # num이 max보다 크면 max에 저장하기
    elif num > max_val:
        max_val = num
# 만약 max가 -1이면 "입력한 숫자가 없습니다." 출력하기
if max_val == -1:
    print("입력한 숫자가 없습니다.")
# 최대값 출력하기
else:
    print(f"최대값: {max_val}")