# 첫 줄은 문자열, 둘째 줄은 정수입니다. 예: "ab" 와 3 → s="ab", n=3
s = input()
n = int(input())


# 문자열 반복 함수 정의하기
def repeat(s, n):
    # 문자열 s와 정수n 곱 반환하기
    return s * n
# 문자열 반복 출력하기
print(repeat(s, n))