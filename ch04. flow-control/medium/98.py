# range(start, end+1)로 반복
start = int(input())
end = int(input())
total = 0
even_sum = 0

# start부터 end까지 반복하기
for i in range(start, end + 1):
    # 전체 합계 구하기
    total += i
    # 만약 i가 2로 나누어 떨어지는 짝수면 다 더하기
    if i % 2 == 0:
        even_sum += i

# 전체 합계 출력하기        
print("구간 합계:", total)
# 짝수 합계 출력하기
print("짝수 합계:", even_sum)
