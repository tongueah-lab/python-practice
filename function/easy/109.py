# 입력을 정수 리스트로 만듭니다. 예: "1 2 3" → nums=[1, 2, 3]
nums = [int(x) for x in input().split()]

# 받은 인자 개수 세기 함수 정의하기
def count_args(*args):
    # 인자 개수 값 반환하기
    return len(args)

# ↓ 호출부 (수정하지 마세요)
print(count_args(*nums))
