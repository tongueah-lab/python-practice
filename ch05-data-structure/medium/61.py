# 좌표를 `(x, y)` tuple로 만든 뒤 dict의 key로 사용해 조회하세요. 존재 여부 확인은 `in` 으로.
positions = {
    (0, 0): 'A',
    (0, 1): 'B',
    (1, 0): 'C',
    (2, 3): 'X',
    (4, 4): 'GOAL',
}
x = int(input())
y = int(input())

# 좌표 변수 만들어 두기
coord = (x, y)
# 좌표를 '(x, y) tuple로 만든 뒤
if coord in positions:
    # 해당 좌표의 값 출력하기
    print(positions[coord])
# 등록되지 않은 좌표면
else:
    # 없음 출력하기
    print("없음")