# key=value 토큰을 dict 로 파싱합니다(값은 문자열). 예: "name=철수 age=20" → opts={"name":"철수","age":"20"}
opts = {}
for token in input().split():
    k, v = token.split("=")
    opts[k] = v

# 회원 등록 함수 정의하기
def register(name, **options):
    # 옵션이 없으면
    if not options:
        # 이름만 반환하기
        return f"{name}:"
    # {이름}={옵션} 사전순으로 , 연결하기
    result = ",".join(f"{k}={v}" for k, v in sorted(options.items()))
    # 반환하기
    return f"{name}: {result}"

# ↓ 호출부 (수정하지 마세요) — name 은 name 매개변수로, 나머지는 **options 로 모임
print(register(**opts))
