# 합이 7인지, 더블인지 순서대로 확인
d1 = int(input())
d2 = int(input())

# 두 주사위 값 출력하기
print(f"주사위: {d1}, {d2}")

# 합이 7이면 럭키세븐! 출력하기
if d1 + d2 == 7:
    print("럭키세븐!")
# 두 값이 같으면 더블! 출력하기
elif d1 == d2:
    print("더블!")
# 그 외면 더해서 출력하기
else:
    total = d1 + d2
    print(f"합: {total}")

