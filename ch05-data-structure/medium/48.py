# 행 우선이므로 바깥 for 가 행(r), 안쪽 for 가 열(c) 입니다.
r = int(input())
c = int(input())

# (R,C) 형식으로 바깥 행 r, 안쪽 열 c를 구분하기
result = [f"({x},{y})" for x in range(r) for y in range(c)]
# 결과 출력하기
print(" ".join(result))