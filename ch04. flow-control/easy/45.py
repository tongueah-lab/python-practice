# 원본 값을 따로 보관하고, while num > 0: num //= 10; count += 1 로 자릿수를 세세요.
num = int(input())
count = 0

# 원본 값을 따로 보관한다. (while문은 원래 값이 보관이 안됨)
original = num

# num을 10씩 나눠서 몇 자리 수가 나오는지 확인한다.
while original > 0:
    original //= 10
    # 나눌때마다 자릿 수 증가
    count += 1
# 최종 자리 수 출력하기
print(f"{num}은(는) {count}자리 수입니다.")