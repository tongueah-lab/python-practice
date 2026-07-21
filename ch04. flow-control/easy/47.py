# 첫 입력을 먼저 받고 while num != 0 으로 반복하며 다음 입력을 받으세요.
total = 0
count = 0

# 첫 입력을 먼저 받기
num = int(input())

# 0이 아니면 입력한 숫자들을 더하고 숫자 갯수도 세기
while num != 0:
    total += num
    count += 1
    # 다음 입력 받기
    num = int(input())
# 입력한 숫자가 없으면 "입력한 숫자가 없습니다." 출력하기
if count == 0:
    print("입력한 숫자가 없습니다.")
# 그 외면 평균을 구하고 출력하기
else:
    total = total/count
    print(f"평균: {total}")
    
    

