# 정수 리스트 nums 를 읽습니다. 예: "5 1 2" → nums=[5, 1, 2]
nums = [int(x) for x in input().split()]

# 2배로 함수 정의하기
def double_first(lst):
    # 첫 원소를 2배로 만드는 식
    lst[0] = lst[0] * 2

# 2배 원소 출력하기
double_first(nums)
# 출력하기
print(nums)