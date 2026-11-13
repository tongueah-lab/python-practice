# 정수 리스트 nums 를 읽습니다. 예: "1 2" → nums=[1, 2]
nums = [int(x) for x in input().split()]

# 새 리스트를 반환하는 함수 정의하기
def add_to_copy(lst):
    # 복사본
    copied = lst[:]
    # 값 반환하기
    copied.append(99)
    return  copied
# 반환된 복사본
print(add_to_copy(nums))
# 원본
print(nums)