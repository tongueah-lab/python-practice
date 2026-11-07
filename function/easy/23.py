# 입력에서 host, port 를 읽습니다(port 는 문자열로 사용). 예: "localhost 8080" → host="localhost", port="8080"
parts = input().split()
host = parts[0]
port = parts[1]

# 아래 함수는 이미 정의되어 있습니다 (수정하지 마세요).
def connect(host, *, port):
    return host + ":" + port

# TODO: port 는 키워드 전용이므로 connect(host, port=port) 로 호출하고, 반환값을 print 하세요.
print(connect(host, port=port))