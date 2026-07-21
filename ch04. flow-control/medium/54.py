# for i in range(len(text)): 조건 만족 시 출력 후 break. found 플래그로 미발견 처리.
text = "hello python"
target = "p"

# 플래그
found = False

# 문자열을 한 글자씩 확인하기
for i in range(len(text)):
    # 타겟을 찾으면 출력하고 반복문 중단하기
    if text[i] == target:
        print(f"'{target}'을(를) {i}번째 위치에서 찾았습니다!")
        found = True
        break

# 발견하지 못하면 출력하기
if not found:
    print("찾지 못했습니다")