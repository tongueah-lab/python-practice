# 정수 리스트 nums 를 읽습니다. 예: "1 2" → nums=[1, 2]
nums = [int(x) for x in input().split()]

#  재할당 함수 정의하기
def reassign(nums):
    # 지역 변수 lst를 새 리스트로 재할당
    lst = [0, 0, 0]
# 변형 함수 정의하기
def mutate(lst):
    # 같은 객체를 직접 변형하여 원본을 바꿉니다.
    lst.append(0)
# reassign 후 nums
reassign(nums)
print(nums)
# mutate 후 nums
mutate(nums)
print(nums)