N, M = map(int, input().split())
a = list(map(int, input().split()))
cnt = 0
for i in range(N):
    sum = 0
    for j in range(i,N):
        sum += a[j]
        if sum >= M:
            if sum == M:
                cnt += 1
            break
print(cnt)
