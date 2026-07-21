# AB형을 A보다 먼저 검사해야 합니다.
blood = input()

# AB형은 "이성적이고 독창적인 성격" 출력하기
if blood == "AB":
    result = "이성적이고 독창적인 성격"
# B형은 "자유롭고 창의적인 성격" 출력하기
elif blood == "B":
    result = "자유롭고 창의적인 성격"
# O형은 "사교적이고 리더십이 강한 성격" 출력하기
elif blood == "O":
    result = "사교적이고 리더십이 강한 성격"
# A형은 "꼼꼼하고 신중한 성격" 출력하기
elif blood == "A":
    result = "꼼꼼하고 신중한 성격"
# 그 외 입력은 "잘못된 입력입니다." 출력하기
else:
    result = "잘못된 입력입니다."

# 잘못된 입력이 아닐때는 "혈액형: \n 성격: "이 출력되게 하기
if result != "잘못된 입력입니다.":
    print(f"혈액형: {blood}형\n성격: {result}")
else:
    print("잘못된 입력입니다.")