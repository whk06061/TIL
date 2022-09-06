import sys
# sys.stdin = open("input.txt")
N = int(sys.stdin.readline())
a = []
idx = [0] * N
result = 0
for i in range(N//2):
    idx[i] = i
    idx[2*(N//2)-i] = i
else:
    idx[i+1] = i+1

for _ in range(N):
    tmp = list(map(int, sys.stdin.readline().split()))
    a.append(tmp)

for i, x in enumerate(idx):
    for j in range(N//2-x, N//2+x+1):
        result += a[i][j]

print(result)