# 음수 인덱스 슬라이싱 `lst[-N:]` 으로 끝 N개를 한 번에 추출합니다.
scores = [85, 92, 78, 95, 88, 70, 100, 65, 82, 90]
n = int(input())


# 끝 n개 출력하기
#print(" ".join([str(x) for x in scores[-n:]]))

print(" ".join(map(str, scores[-n:])))