# 전역 total 시작값 0. 더할 정수들을 리스트로 읽습니다. 예: "1 2 3 4" → nums=[1, 2, 3, 4]
total = 0
nums = [int(x) for x in input().split()]

# TODO: global total 로 누적하는 add(n) 을 정의하고, 각 수에 add 호출 후 total 을 print 하세요.
# 함수 정의하기
def add(n):
    # global total로 누적하는
    global total
    # add(n)을 정의하고
    total += n
# 각 수에 add호출 후
for n in nums:
    add(n)
# total을 호출하기
print(total)