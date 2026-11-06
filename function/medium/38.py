# 전역 name = 첫 단어, age = 둘째 단어. 예: "철수 20" → name="철수", age="20"
parts = input().split()
name = parts[0]
age = parts[1]

# 함수 정의하기
def describe():
    # 이름, 나이 값 반환하기
    return f"{name}({age})"
# 결과 출력하기
print(describe())