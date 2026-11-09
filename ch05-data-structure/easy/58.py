# `a, b = b, a` 한 줄로 임시 변수 없이 두 값을 동시에 교환합니다.
a = int(input())
b = int(input())

# 교환 전 출력하기
print(f"교환 전: a={a} b={b}")

# 내부적으로 (b, a) tuple이 생성된 후 a, b에 동시 언패킹됩니다.
a, b = b, a

# 교환 후 출력하기
print(f"교환 후: a={a} b={b}")