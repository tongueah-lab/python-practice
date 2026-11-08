# 위치: 첫째=이름, 나머지=역할. "status=값" 은 키워드 전용 상태, 그 외 "key=값" 은 메타 정보(meta).
# 예: "김철수 개발 디자인 status=휴직 dept=IT" → name=김철수, roles=[개발,디자인], status=휴직, meta={dept:IT}
raw = input().split()
pos = [t for t in raw if "=" not in t]
name = pos[0]
roles = pos[1:]
status = "active"
meta = {}
for t in raw:
    if "=" in t:
        k, v = t.split("=", 1)
        if k == "status":
            status = v
        else:
            meta[k] = v



# 사용자 프로필 함수 정의하기
def profile(name, *roles, status="active", **meta):
    # 이름, 임의 개수의 역할, 상태, 그리고 그 외 메타 정보를 받아 프로필 요약을 반환하기
    return f"{name}[{status}] 역할{len(roles)} 정보{len(meta)}"
# ↓ 호출부 (수정하지 마세요)
print(profile(name, *roles, status=status, **meta))
