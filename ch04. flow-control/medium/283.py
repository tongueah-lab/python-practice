# range는 음수 step을 지원합니다. 1 미만으로 내려가지 않도록 종료값을 설정하세요.
n = int(input())
k = int(input())

# n부터 1이상의 값까지 k만큼 감소시키기
for i in range(n, 0, -k):
    # 한 줄에 공백으로 구분하여 출력하기
    print(i, end=" ")

# 한 줄 띄우고 발사 출력하기
print()
print("발사!")