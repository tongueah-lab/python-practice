# 전역 total, peak 시작값 0. 변화량들을 순서대로 읽습니다. 예: "5 -3 10" → parts=["5","-3","10"]
parts = input().split()
total = 0
peak = 0

# TODO: global total, peak 로 누적합과 최고치를 추적하는 step(delta) 를 정의하고,
#   각 변화량을 처리한 뒤 total 과 peak 를 두 줄로 print 하세요.

# 함수 정의하기
def step(delta):
    # global total, peak 선언 후
    global total, peak
    # total += delta
    total += delta

    # total > peak이면
    if total > peak:
        # peak = total
        peak = total
    
# 숫자들을 하나씩 꺼내기
for i in parts:
    # step에 넣기
    step(int(i))
    
# 최종 total 출력하기
print(total)
# peak 출력하기
print(peak)