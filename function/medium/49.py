# 전역 x=첫 값, a=둘째, b=셋째. 예: "10 20 30" → x=10, a=20, b=30
parts = input().split()
x = int(parts[0])
a = int(parts[1])
b = int(parts[2])

# without_global(a) 호출하기
def without_global(v):
    x = v
# with_global(b) 호출하기
def with_global(v):
    global x
    x = v

# without_global 호출 후 x 출력하기
without_global(a)
print(x)

# with_global 호출 후 x 출력하기
with_global(b)
print(x)