# 입력에서 base, exp 를 읽습니다. 예: "2 10" → base=2, exp=10
parts = input().split()
base = int(parts[0])
exp = int(parts[1])

# 아래 함수는 이미 정의되어 있습니다 (수정하지 마세요).
def power(base, *, exp):
    return base ** exp

# TODO: exp 는 키워드 전용이므로 power(base, exp=exp) 로 호출하고, 반환값을 print 하세요.
print(power(base, exp=exp))