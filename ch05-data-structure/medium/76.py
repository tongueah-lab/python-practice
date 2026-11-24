# `counts[w] = counts.get(w, 0) + 1` 패턴이 dict 빈도 카운트의 정석입니다.
words = input().split()
# TODO

# 카운트 리스트 만들기
counts = {}

# 단어 순회하기
for w in words:
    counts[w] = counts.get(w, 0) + 1

# counts.iteam() 순회해서 단어: 횟수 출력하기
for word, count in counts.items():
    print(f"{word}: {count}")