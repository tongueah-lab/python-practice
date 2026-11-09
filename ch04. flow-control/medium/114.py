# 위 규칙을 그대로 구현
seed = int(input())

# 변수 n1 저장하기
n1 = (seed * 7 + 3) % 45 + 1

# 변수 n2 저장하기
n2 = (n1 * 13 + 11) % 45 + 1
if n2 == n1:
    n2 = n2 % 45 + 1

# 변수 n3 저장하기
n3 = (n2 * 17 + 7) % 45 + 1
if n3 == n2 or n3 == n1: 
    n3 = n3 % 45 + 1

if n3 == n2 or n3 == n1: 
    n3 = n3 % 45 + 1

# 변수 n4 저장하기
n4 = (n3 * 23 + 5) % 45 + 1
if n4 == n3 or n4 == n2 or n4 == n1:
    n4 = n4 % 45 + 1

if n4 == n3 or n4 == n2 or n4 == n1:
    n4 = n4 % 45 + 1

# 변수 n5 저장하기
n5 = (n4 * 29 + 13) % 45 + 1
if n5 == n4 or n5 == n3 or n5 == n2 or n5 == n1:
    n5 = n5 % 45 + 1

if n5 == n4 or n5 == n3 or n5 == n2 or n5 == n1:
    n5 = n5 % 45 + 1

# 변수 n6 저장하기
n6 = (n5 * 31 + 17) % 45 + 1
if n6 == n5 or n6 == n4 or n6 == n3 or n6 == n2 or n6 == n1:
    n6 = n6 % 45 + 1

if n6 == n5 or n6 == n4 or n6 == n3 or n6 == n2 or n6 == n1:
    n6 = n6 % 45 + 1


# 로또 번호 표지 출력하기
print("=== 로또 번호 ===")
print(f"번호 1: {n1}")
print(f"번호 2: {n2}")
print(f"번호 3: {n3}")
print(f"번호 4: {n4}")
print(f"번호 5: {n5}")
print(f"번호 6: {n6}")
print("행운을 빕니다!")