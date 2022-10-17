from difflib import restore
import sys
sys.stdin = open("input.txt", "r")
n, m = map(int, input().split())
data = list(map(int, input().split()))
count = [0] * (m+1)
result = 0
data.sort()
for x in data:
    count[x] += 1
for i in range(1, m+1):
    n = n - count[i]
    result += n * count[i]
print(result)
