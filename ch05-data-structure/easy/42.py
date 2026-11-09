# 문자열도 시퀀스이므로 `for c in s` 로 한 글자씩 순회할 수 있습니다. 숫자/기호는 upper() 영향을 받지 않습니다.
s = input()

# 각 글자를 대문자로 변환하기
result = [ch.upper() for ch in s]

# 출력하기
print(" ".join(result))