# 전역 amount = 첫 값, rate = 둘째 값. 예: "1000 10" → amount=1000, rate=10
parts = input().split()
amount = int(parts[0])
rate = int(parts[1])


# 전역변수만으로 계산 함수 정의하기
def tax_of():
    # 두 전역 사용, 정수 나눗셈 값 반환하기
    return amount * rate // 100
# 결과 출력하기
print(tax_of())