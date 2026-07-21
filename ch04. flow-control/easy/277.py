# 바깥 if는 배차 가능 여부, 안쪽 if는 목적지 유무로 작성하세요.
available = input() == "True"
destination = input()

# 배차 가능하면
if available:
    # 목적지가 비어있지 않으면 "운행 시작" 출력하기
    if destination:
        print("운행 시작")
    # 비어있으면 "목적지를 입력하세요" 출력하기
    else:
        print("목적지를 입력하세요")
# 배차 불가능하면 "차량 대기 중" 출력하기
else:
    print("차량 대기 중")