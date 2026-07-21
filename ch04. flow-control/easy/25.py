# 맞는 아이디, 비밀번호 저장하기
correct_id = "admin"
correct_password = "1234"

# 중첩 if문으로 아이디를 먼저, 그 안에서 비밀번호를 확인하세요.
user_id = input()
password = input()

# 아이디가 맞으면 비밀번호 확인하기
if user_id == correct_id:
    # 비밀번호가 맞으면 "로그인 성공!" 출력하기
    if password == correct_password:
        print("로그인 성공!")
    # 비밀번호가 틀리면 "비밀번호가 틀렸습니다." 출력하기
    else:
        print("비밀번호가 틀렸습니다.")
# 아이디가 틀리면 "ID가 존재하지 않습니다." 출력하기
else:
    print("ID가 존재하지 않습니다.")