# 입력을 단어 리스트로 만듭니다. 예: "a b c" → words=["a", "b", "c"]
words = input().split()

# 함수 정의하기
def concat_words(*words):
    # 단어들을 -로 이은 문자열을 반환하기
    return "-".join(words)

# ↓ 호출부 (수정하지 마세요)
print(concat_words(*words))
