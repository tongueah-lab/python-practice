# 이미 있는 키에 다시 대입하면 값이 갱신됩니다.
scores = {"윤서": 85, "지우": 92, "민준": 65, "서윤": 78, "도윤": 95}
name = input()
new_score = int(input())

# 점수 리스트의 점수를 새로운 점수로 갱신하기
scores[name] = new_score
# 결과 출력하기
print(f"{name}: {new_score}")