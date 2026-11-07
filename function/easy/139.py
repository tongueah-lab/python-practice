# key=value 토큰을 dict 로 파싱합니다. 예: "greeting=안녕 name=철수" → opts={"greeting":"안녕","name":"철수"}
opts = {}
for token in input().split():
    k, v = token.split("=")
    opts[k] = v

# 함수 정의하기
def greet(greeting, name):
    # 인사 ,구분하고 이름 ! 값 반환하기
    return greeting + ", " + name + "!"

# TODO: opts 를 ** 로 풀어 greet 에 넘기고, 그 반환값을 print 하세요.
print(greet(**opts))