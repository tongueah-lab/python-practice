# float로 입력받아 구간별로 판정하세요.
distance = float(input())

# 2km 미만은 도보가 출력되게 하기
if distance < 2:
    result = "도보"
# 2km 이상 5km 미만은 자전거가 출력되게 하기
elif distance < 5:
    result = "자전거"
# 5km 이상 20km 미만은 버스가 출력되게 하기
elif distance < 20:
    result = "버스"
# 20km 이상은 지하철이 출력되게 하기
else:
    result = "지하철"

print(f"거리: {distance}km")
print(f"추천 교통수단: {result}")