# f-string 정렬: `:<폭` 왼쪽, `:>폭` 오른쪽, `:^폭` 가운데
name = input()
opt = input()

# L: 왼쪽 정렬
if opt == "L":
    print(f"|{name:<10}|")
# R: 오른쪽 정렬
elif opt == "R":
    print(f"|{name:>10}|")
# C: 가운데 정렬
elif opt == "C":
    print(f"|{name:^10}|")