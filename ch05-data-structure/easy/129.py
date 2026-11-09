# zip 또는 인덱스 순회로 (이름, 점수) 쌍을 보면서 조건 만족하는 이름만 모으세요.
names  = ["윤서", "지우", "민준", "서윤", "도윤"]
scores = [85, 92, 65, 78, 95]
n = int(input())

# 점수가 n 이상인 학생 이름
for name, score in zip(names, scores):
    # 점수가 n이상이면
    if score >= n:
        # 이름 공백 구분으로 한 줄에 출력하기
        print(name, end = " ")
    