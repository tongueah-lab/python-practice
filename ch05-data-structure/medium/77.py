# items()로 (이름, 점수)를 순회하면서 일치하는 이름만 모아 출력하세요.
scores = {"윤서": 85, "지우": 92, "민준": 85, "서윤": 78, "도윤": 92, "예준": 65}
x = int(input())

# 타겟 리스트 만들기
target_name = []

# 점수 리스트를 이름, 점수로 순회하기
for name, score in scores.items():
    # 입력받은 점수랑 점수가 같으면
    if x == score:
        # 타겟 리스트에 해당 학생 추가하기
        target_name.append(name)
    
# 입력받은 점수가 리스트 점수에 있으면
if target_name:
    # 그 이름 출력하기
    print(" ".join(target_name))
# 해당 학생이 없으면
else:
    # 없음 출력하기
    print("없음")