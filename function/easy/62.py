"""`)로 작성하시오. 그런 다음 다음 두 줄을 출력하시오.

1. `add.__doc__` (작성한 docstring 내용)
2. `add(a, b)` 의 반환값

- docstring 은 함수 설명을 코드 안에 남기는 방법이며 `함수명.__doc__` 로 읽을 수 있다.
- 예: 입력 `3 5` → 첫 줄 `두 정수의 합을 반환한다.`, 둘째 줄 `8`

함수 명세
- 이름: `add(a, b)` — 첫 줄 docstring `두 정수의 합을 반환한다.`, 본문 `return a + b`
- 출력: 첫 줄 = `add.__doc__`, 둘째 줄 = `add(a, b)`
"""

# 두 정수를 읽습니다. 예: "3 5" → a=3, b=5
parts = input().split()
a = int(parts[0])
b = int(parts[1])

#  docstring "두 정수의 합을 반환한다." 를 가진 add(a, b) 를 정의하고,
#  add.__doc__ 와 add(a, b) 를 두 줄로 print 하세요. 

# 함수 정의하기
def add(a, b):
    # docstring 적기
    '''두 정수의 합을 반환한다.'''
    # 값 반환하기
    return a + b

# 결과 출력하기
print(add.__doc__)
print(add(a, b))