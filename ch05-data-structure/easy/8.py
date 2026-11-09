# `index` 메서드는 없는 값을 찾으면 오류가 발생하므로, 먼저 `in`으로 존재 여부를 확인하세요.
names = ["윤서", "지우", "민준", "서윤", "도윤", "예준"]
name = input()

# names 리스트에 입력한 name이 있다면
if name in names:
    # 몇 번째에 있는지 출력하기
    print(f"{names.index(name)+1}번째에 있습니다")
# 없으면 없다고 출력하기
else:
    print("명단에 없습니다")