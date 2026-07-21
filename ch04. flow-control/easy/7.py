# "예"로 답한 재료만 이어 붙여 "나의 파스타: ..." 형식으로 출력하세요.
add_cheese = input()
add_bacon = input()
add_shrimp = input()
pasta = "파스타"

# if문을 사용해 치즈 추가 여부 묻기
if add_cheese == "예":
    pasta += " + 치즈"
# if문을 사용해 베이컨 추가 여부 묻기
if add_bacon == "예":
    pasta += " + 베이컨"
# if문을 사용해 새우 추가 여부 묻기
if add_shrimp == "예":
    pasta += " + 새우"

# 추가에 예로 답한 재료만 +형식으로 이어붙여 "나의 파스타" 형식으로 출력하기
print(f"나의 파스타: {pasta}")