# 문자열은 리스트와 동일한 슬라이싱 문법을 지원합니다.
s = input()

# 슬라이싱으로 처음 끝 중간 문자열 출력하기
start = s[:3]
end = s[-3:]
middle = s[3:-3]

print(f"처음 3: {start}")
print(f"끝 3: {end}")
print(f"가운데: {middle}")