# lower()로 소문자 변환 후 비교
text = input()
vowel_count = 0

# 대소문자 모음을 리스트로 만들기
vowel = ["a","e","i","o","u","A","E","I","O","U"]

# 입력한 문자를 한 글자씩 순회하기
for char in text:
    # 문자에 모음이 있으면 카운트 세기
    if char in vowel:
        vowel_count += 1
# 모음 개수 출력하기
print(f"모음 개수: {vowel_count}")