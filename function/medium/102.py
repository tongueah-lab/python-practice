# 한 줄을 공백으로 나눕니다. 토큰 1/2/3 개에 따라 age, city 가 기본값으로 채워집니다. (age 는 정수)
parts = input().split()

# 자기소개 함수 정의하기
def introduce(name, age=20, city="서울"):
    # 값 반환하기
    return f"{name}/{age}/{city}"

# 토큰 1개 이름
if len(parts) == 1:
    print(introduce(parts[0]))
# 토큰 2개 이름 나이
elif len(parts) == 2:
    print(introduce(parts[0], parts[1]))
# 토큰 3개 이름 나이 도시
else:
    print(introduce(parts[0], int(parts[1]), parts[2]))