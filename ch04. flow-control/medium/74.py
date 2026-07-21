# 나이로 기준을 먼저 나누세요.
height = float(input())
weight = float(input())
age = int(input())

# BMI 계산식잡기
bmi = weight / ((height/100)**2)

# 나이가 20살 이상이고
if age >= 20:
    # BMI가 18.5 미만이면 저체중이다.
    if bmi < 18.5:
        result = "판정: 저체중"
    # BMI가 23 미만이면 정상이다.
    elif bmi < 23:
        result = "판정: 정상"
    # BMI가 25 미만이면 과체중이다.
    elif bmi < 25:
        result = "판정: 과체중"
    # 그 외는 비만이다
    else:
        result = "판정: 비만"

# 나이가 20살 미만이고
else:
    # BMI가 17 미만이면 저체중이다.
    if bmi < 17:
        result = "판정: 저체중 (청소년 기준)"
    # BMI가 23 미만이면 정상이다.
    elif bmi < 23:
        result = "판정: 정상 (청소년 기준)"
    # 그 외는 과체중이다.
    else:
        result = "판정: 과체중 주의 (청소년 기준)"

# "BMI: " 소수점 둘쩨자리까지 출력하기
print(f"BMI: {round(bmi, 2)}")
# 판정 출력하기
print(result)