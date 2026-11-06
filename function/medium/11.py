# 위치 토큰: 첫째=제목, 나머지=정수. "unit=값" 은 키워드 전용 단위.
# 예: "거리 10 20 unit=km" → title="거리", values=[10,20], unit="km"
raw = input().split()
pos = [t for t in raw if "=" not in t]
title = pos[0]
values = [int(x) for x in pos[1:]]
unit = "개"
for t in raw:
    if "=" in t:
        k, v = t.split("=", 1)
        if k == "unit":
            unit = v

# 함수 report(title, *values, unit="개") 를 직접 정의(def)하기
def report(title, *values, unit=unit):
    # title과 values 합계, unit을 조합한 문자열을 반환한다.
    return f"{title}: {sum(values)}{unit}"

# ↓ 호출부 (수정하지 마세요) — unit 은 키워드 전용이라 이름으로 전달
print(report(title, *values, unit=unit))
