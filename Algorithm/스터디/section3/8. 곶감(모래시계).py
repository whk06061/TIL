import sys
sys.stdin = open("input.txt")
N = int(sys.stdin.readline())
a = []
for _ in range(N):
    tmp = list(map(int,sys.stdin.readline().split()))
    a.append(tmp)
M = int(sys.stdin.readline())
for _ in range(M):
    line, direction, num = map(int, sys.stdin.readline().split())
    line = line-1
    tmp = [0] * N
    for j in range(N):
        if direction == 0:
            if j < num:
                tmp[j + N - num] = a[line][j]
            else:
                tmp[j-num] = a[line][j]
        else:
            if j < N-num:
                tmp[j+num] = a[line][j]
            else:
                tmp[j - N + num] = a[line][j]
    for j in range(N):
        a[line][j] = tmp[j]

