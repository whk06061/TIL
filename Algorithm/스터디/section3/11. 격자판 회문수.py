import sys
#sys.stdin = open("input.txt", "rt")
a = []
cnt = 0
def check(x):
    global cnt
    for m in range(0,2):
        if x[m] != x[4-m]:
            break
    else:
        cnt += 1

for _ in range(7):
    tmp = list(map(int, input().split()))
    a.append(tmp)

# 행에서 찾기
for i in range(7):
    for j in range(3):
        tmp = a[i][j:j+5]
        check(tmp)

# 열에서 찾기
for i in range(7):
    for j in range(3):
        tmp = []
        for k in range(5):
            tmp.append(a[j+k][i])
        check(tmp)
print(cnt)

