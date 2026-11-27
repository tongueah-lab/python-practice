# 학생 존재 여부와 과목 존재 여부를 각각 검사한 뒤 `students[name][subject]` 로 조회하세요.
students = {
    "윤서": {"수학": 85, "영어": 90, "과학": 78},
    "지우": {"수학": 92, "영어": 88},
    "민준": {"수학": 65, "영어": 70, "과학": 80, "역사": 75},
}
name = input()
subject = input()

# 만약 이름이 학생 리스트에 있고 과목이 학생 리스트 이름에 있으면
if name in students and subject in students[name]:
    # 점수 출력하기
    print(students[name][subject])
# 그렇지 않으면
else:
    # "없음" 출력하기
    print("없음")