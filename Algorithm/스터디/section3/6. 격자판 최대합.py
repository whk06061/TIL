import sys
# sys.stdin = open("input.txt")
N = int(sys.stdin.readline())
a = []
result = 0

for _ in range(N):
    tmp = list(map(int, sys.stdin.readline().split()))
    a.append(tmp)

# 열 합 구하기  
for i in range(N):
    tmp = 0
    for arr in a:
        tmp += arr[i]
    if tmp > result:
        result = tmp

# 행 합 구하기
for arr in a:
    tmp = sum(arr)
    if tmp > result:
        result = tmp

# 왼쪽 대각선 구하기
for i in range(N):
    tmp = 0
    tmp += a[i][i]
if tmp > result:
        result = tmp

# 오른쪽 대각선 구하기
for i in range(N-1,-1,-1):
    tmp = 0
    tmp += a[i][i]
if tmp > result:
        result = tmp

print(result)