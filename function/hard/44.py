# 전역 language = 첫 단어, chosen = 둘째 단어. 예: "한국어 영어" → language="한국어", chosen="영어"
parts = input().split()
language = parts[0]
chosen = parts[1]

# setting() 내부에서
def setting():
    # 지역변수 language = chosen으로 두고
    language = chosen
        # "현재: " + language 반환하기
    return "현재: " + language
# reading() 지역변수를 만들지 않고
def reading():
    # "기본: " + language 반환하기
    return "기본: " + language

# setting() 반환값 출력하기
print(setting())
# reading() 반환값 출력하기
print(reading())
# 전역 language
print(language)