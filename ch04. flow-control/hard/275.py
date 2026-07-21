# 실패/특수 조건을 먼저 걸러내는 순서가 중요합니다. 조건 결합은 and 를 사용하세요.
is_employed = input() == "True"
salary = int(input())
credit_grade = int(input())

# 직장인이 아니면 "직장인 확인 필요" 출력하기
if not is_employed:
    print("직장인 확인 필요")
    
# 연봉 3000만원 미만이면 "연봉 조건 미달" 출력하기
elif salary < 3000:
    print("연봉 조건 미달")

# 연봉 3000만원 이상, 신용등급이 3등급 이하면
elif salary >= 3000 and credit_grade <= 3:
    # "대출 한도: 5000만원" 출력하기
    print("대출 한도: 5000만원")
        
# 연봉 5000만원 이상, 신용등급 4등급 이상이면
elif salary >= 5000 and credit_grade >= 4:
    # "대출 한도: 3000만원" 출력하기
    print("대출 한도: 3000만원")

# 연봉 3000만원 이상 5000만원 미만, 신용등급 4등급 이상인 경우
else:
    # "대출 한도: 1000만원" 출력하기
    print("대출 한도: 1000만원")




