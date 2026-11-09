# `text.find(target)` 은 없으면 -1을 반환하므로 안전하게 사용할 수 있습니다.
text = input()
target = input()

# 부분문자열 위치 찾아서 출력하기
print(text.find(target))