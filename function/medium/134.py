# key=value 토큰을 dict 로 파싱합니다(값은 문자열). 예: "b=2 a=1" → opts={"b":"2","a":"1"}
opts = {}
for token in input().split():
    k, v = token.split("=")
    opts[k] = v

# 함수 정의하기
def merge_to_string(**kwargs):
    # 키=값으로 만들고 키 사전순으로 정렬해 ","로 연결하기
    return ",".join(f"{k}={v}" for k, v in sorted(kwargs.items()))

# ↓ 호출부 (수정하지 마세요) — opts 를 ** 로 풀어 키워드 인자로 전달
print(merge_to_string(**opts))
