# input() 으로 이름 한 줄을 읽습니다. 예: 입력이 "철수" 이면 name == "철수"
name = input()

# 인사말을 반환하는 함수를 정의하기
def greet(name):
    # return으로 값 반환하기
    return f"안녕하세요, {name}님!"
# 결과 출력하기
print(greet(name))