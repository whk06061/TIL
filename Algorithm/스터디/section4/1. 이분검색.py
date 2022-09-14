import sys
#sys.stdin = open("input.txt", "r")
n, m  = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
s = 0
e = n-1
while True:
    p = (s + e)//2
    if a[p] > m :
        e = p-1
    elif a[p] < m :
        s = p+1
    else:
        print(p+1)
        break