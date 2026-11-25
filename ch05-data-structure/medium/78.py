# update() 의 결과는 None — main 이 직접 변경됩니다.
main_sets = [
    {"수학": 80, "영어": 75, "과학": 90},
    {"A": 1, "B": 2},
    {"X": 10, "Y": 20},
]
update_sets = [
    {"영어": 88, "역사": 70},
    {"C": 3, "D": 4},
    {},
]
t = int(input())
main = main_sets[t]
update_data = update_sets[t]

# main을 그 자리에서 변경(덮어쓰기 + 새 키 추가)
main.update(update_data)

# 순회하기
for k, v in main.items():
    # 키: 값 출력하기
    print(f"{k}: {v}")