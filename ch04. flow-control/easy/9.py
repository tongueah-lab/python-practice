# 컴퓨터는 "바위" 고정. 사용자 입력과 비교하여 결과를 출력하세요.
computer = "바위"
user = input()

# 사용자가 바위를 내면 결과는 "비겼습니다"
if user == "바위":
    result = "비겼습니다"
# 사용자가 가위면 결과는 "졌습니다"
elif user == "가위":
    result = "졌습니다"
# 사용자가 보를 내면 결과는 "이겼습니다"
elif user == "보":
    result = "이겼습니다"
# 그 외 입력은 결과는 "잘못된 입력입니다"
else:
    result = "잘못된 입력입니다"

# "컴퓨터: "의 값 출력하기
print(f"컴퓨터: {computer}")
# "나: "의 값 출력하기
print(f"나: {user}")
# "결과: "값 출력하기
print(f"결과: {result}")