# f-string은 `f"...{변수}..."` 형태로 문자열 안에서 변수를 그대로 사용할 수 있습니다.
name = input()
score = int(input())

# 이름, 점수 출력하기
print(f"이름: {name}, 점수: {score}")