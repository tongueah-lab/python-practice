# `data[i:i+w]` 으로 한 번에 윈도우 슬라이스를 얻습니다.
data = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
i = int(input())
w = int(input())
# 윈도우 슬라이스 출력하기
print(' '.join(map(str, data[i:i+w])))

