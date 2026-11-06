# input() 으로 문자열 한 줄을 읽습니다. 예: 입력이 "hello" 이면 s == "hello"
s = input()

# 모음 개수 세기 함수 정의하기
def count_vowels(s):
    # 카운트 초기화하기
    count = 0
    # 모음 정리하기
    vowels = "aeiou"

    # 문자열 s반복하기
    for char in s:
        # 문자열에 모음이 있으면
        if char in vowels:
            # 카운터 세기
            count += 1

    # 값 반환하기
    return count

# 결과 출력하기
print(count_vowels(s))