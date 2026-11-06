# 전역 prefix=첫, text=둘째, inner_prefix=셋째. 예: "[G] 제목 [L]" → prefix="[G]", text="제목", inner_prefix="[L]"
parts = input().split()
prefix = parts[0]
text = parts[1]
inner_prefix = parts[2]

# TODO: 지역 prefix=inner_prefix 로 가리고 전역 text 를 읽어 반환하는 label() 을 정의한 뒤,
#   label() 반환값과 전역 prefix 를 두 줄로 print 하세요.

# label 정의하기
def label():
    # 지역 변수
    prefix = inner_prefix
    # 지역 변수 + 전역 변수 값 반환하기
    return prefix + text
# 결과 출력하기
print(label())
print(prefix)