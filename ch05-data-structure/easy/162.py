# 두 set 각각에 대해 `in` 으로 검사한 결과를 조합해 분기하세요.
club_a = {"윤서", "지우", "민준", "도윤"}
club_b = {"지우", "민준", "예준", "하준"}
name = input()

# 변수로 저장하기
in_a = name in club_a
in_b = name in club_b
# 동아리a와 동아리b에 이름이 있으면
if in_a and in_b:
    # "양쪽 모두" 출력하기
    print("양쪽 모두")
# 동아리a에만 이름이 있으면
elif in_a:
    # "a 동아리만" 출력하기
    print("A 동아리만")
# 동아리b에만 이름이 있으면
elif in_b:
    # "b 동아리만" 출력하기
    print("B 동아리만")
# 둘 다 없으면
else:
    # "미가입" 출력하기
    print("미가입")