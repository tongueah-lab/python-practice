# 빈 리스트에서 시작해 N번 입력을 받아 append로 추가하세요. 출력 시 join을 활용하면 깔끔합니다.
n = int(input())


# 빈 리스트 만들기
name_list = []
# n번 반복하기
for _ in range(n):
    # 이름 입력받기
    name = input()
    # 빈 리스트에 이름들 추가하기
    name_list.append(name)
# 출석 몇 명인지 출력하기
print(f"출석 {n}명")
# 명단 출력하기
print("명단: " + " ".join(name_list))