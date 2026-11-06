# 전역 name = 첫 단어, guest = 둘째 단어. 예: "주인 손님" → name="주인", guest="손님"
parts = input().split()
name = parts[0]
guest = parts[1]

# TODO: 매개변수 name 을 받는 greet(name) 을 정의한 뒤, greet(guest) 반환값과 전역 name 을 두 줄로 print 하세요.

# 함수 정의하기
def greet(name):
    # 매개변수 name을 사용해 반환
    return "안녕, " + name
# 인사 결과 출력하기
print(greet(guest))
# 이름 출력하기
print(name)