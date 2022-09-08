import sys
#sys.stdin = open("input.txt")
N = int(input())
a = []
a.append([0]*(N+2))
cnt = 0
for _ in range(N):
    tmp = [0]
    tmp += list(map(int, input().split()))
    tmp.append(0)
    a.append(tmp)
a.append([0]*(N+2))
for i in range(1,N+1):
    for j in range(1,N+1):
        cur = a[i][j]
        if cur > a[i-1][j] and cur > a[i][j-1] and cur > a[i+1][j] and cur > a[i][j+1]:
            cnt += 1
print(cnt)