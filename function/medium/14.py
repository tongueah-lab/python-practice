# 위치 토큰: 첫째=이벤트, 나머지=상세. "level=값" 은 키워드 전용 레벨.
# 예: "에러 파일없음 권한 level=ERROR" → event="에러", details=["파일없음","권한"], level="ERROR"
raw = input().split()
pos = [t for t in raw if "=" not in t]
event = pos[0]
details = pos[1:]
level = "INFO"
for t in raw:
    if "=" in t:
        k, v = t.split("=", 1)
        if k == "level":
            level = v

# TODO: 여기에 함수 log_event(event, *details, level="INFO") 를 직접 정의(def)하세요. (아래 호출이 동작해야 함)

# 이벤트 로그 함수 정의하기
def log_event(event, *details, level="INFO"):
    # 값 반환하기
    return f"{level}: {event} ({len(details)})"
# ↓ 호출부 (수정하지 마세요) — level 은 키워드 전용이라 이름으로 전달
print(log_event(event, *details, level=level))
