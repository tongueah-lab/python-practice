# input().split() 으로 두 칸을 나눠 각각 정수로 바꿉니다. 예: "10 3" → a=10, b=3
first_num, second_num = [int(x) for x in input().split()]

# 함수 정의하기
def difference(first_num, second_num):
    # 두 수의 차 값 반환하기
    return first_num - second_num

# 두 수의 차 출력하기
print(difference(first_num, second_num))