# 첫 값=정수 n, 나머지=리스트 items. 예: "5 1 2" → n=5, items=[1, 2]
parts = input().split()
n = int(parts[0])
items = [int(x) for x in parts[1:]]


# change_both(num, lst)(num+100, lst.append(0))를 정의하기
def change_both(num, lst):
    num = num + 100
    lst.append(0)

# 원본n (그대로), items(0추가됨) 호출하기
change_both(n, items)

# 결과 출력하기
print(n)
print(items)