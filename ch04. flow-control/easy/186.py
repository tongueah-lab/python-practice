# 총 초를 입력받아 HH:MM:SS 형식으로 출력하세요.
total_seconds = int(input())

# 한 시간 = 총 초 // 3600(1시간)
hour = total_seconds // 3600

# 남은 초 = 전체 초 % 3600(1시)
remain = total_seconds % 3600

# 분() = 나머지 초 // 60(1분)
minutes = remain // 60

# 초 = 나머지 초 % 60
secs = remain % 60

# 02d(d는 정수로 출력, 2는 두자리로 출력, 0은 빈 자리는 0으로 채움)
print(f"{hour:02d}:{minutes:02d}:{secs:02d}")