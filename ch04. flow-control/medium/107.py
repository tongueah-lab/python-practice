# 바깥 for는 선택, 안쪽 for는 개수 세기
text = input()

# 바깥 for문으로 문자열 훑기
for char in text:
    # 개수 초기 값 잡기
    count = 0
    # 안쪽 for문으로 하나하나 문자열 훑기
    for inner_char in text:
        # 만약 바깥 for문과 안쪽 for문이 같다면
        if char == inner_char:
            # 개수 세기
            count += 1
    # 문자열 하나씩 몇 번 나오는지 출력하기
    print(f"{char}: {count}개")