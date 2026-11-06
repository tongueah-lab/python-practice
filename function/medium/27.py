# 마지막 토큰=구분자(sep), 나머지=값들(values). 예: "a b c +" → values=["a","b","c"], sep="+"
parts = input().split()
values = parts[:-1]
sep = parts[-1]

# 아래 함수는 이미 정의되어 있습니다 (수정하지 마세요).
def join_all(*values, sep):
    return sep.join(values)

# TODO: values 는 * 로 풀고 sep 는 키워드로 — join_all(*values, sep=sep) 로 호출하고 print 하세요.

print(join_all(*values, sep=sep))