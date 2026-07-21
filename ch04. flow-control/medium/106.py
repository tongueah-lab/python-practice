# 뒤집은 문자열과 원본을 비교
text = input()
reversed_text = ""

# (start, step, stop) 역순 순회하기
for char in range(len(text)-1, -1, -1):
    # 뒤집은 문자열을 다시 합치기
    reversed_text += text[char]

# 문자열과 뒤집은 문자열이 똑같은면 회문이라고 출력하기
if text == reversed_text:
    print(f"{text}은(는) 회문입니다!")
# 아니면 회문이 아니라고 출력하기
else:
    print(f"{text}은(는) 회문이 아닙니다.")