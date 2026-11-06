# 위치 토큰: 첫째=endpoint, 나머지=args. "method=값" 은 method, 그 외 "key=값" 은 headers.
# 예: "/users id name method=POST token=abc" → endpoint="/users", args=["id","name"], method="POST", headers={"token":"abc"}
raw = input().split()
pos = [t for t in raw if "=" not in t]
endpoint = pos[0]
args = pos[1:]
method = "GET"
headers = {}
for t in raw:
    if "=" in t:
        k, v = t.split("=", 1)
        if k == "method":
            method = v
        else:
            headers[k] = v

# 아래 함수는 이미 정의되어 있습니다 (수정하지 마세요).
def api(endpoint, *args, method="GET", **other):
    return endpoint + " " + method + " a" + str(len(args)) + " h" + str(len(other))

# TODO: api(endpoint, *args, method=method, **headers) 로 호출하고, 반환값을 print 하세요.
print(api(endpoint, *args, method=method, **headers))