# 첫 토큰=제목, 마지막 토큰=단위, 가운데=정수 값들. 예: "매출 10 20 30 원" → title="매출", values=[10,20,30], unit="원"
parts = input().split()
title = parts[0]
values = [int(x) for x in parts[1:-1]]
unit = parts[-1]

# 아래 함수는 이미 정의되어 있습니다 (수정하지 마세요).
def report(title, *values, unit):
    s = 0
    for v in values:
        s += v
    return title + ": " + str(s) + unit

# TODO: report(title, *values, unit=unit) 로 호출하고, 반환값을 print 하세요.
print(report(title, *values, unit=unit))