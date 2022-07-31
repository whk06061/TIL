import sys

# 1. 같은 눈 세개 : 10,000 + 같은 눈 * 1,000
# 2. 같은 눈 두개 : 1,000 + 같은 눈 * 100
# 3. 모두 다른 눈 : 그 중 가장 큰 눈 * 100

# a, b, c = map(int, input().split())

# if a == b == c: print(10000 + a * 1000)
# else:
#     if a==b or a==c: print(1000 + a * 100)
#     elif b==c: print(1000 + b * 100)
#     else: 
#         list = [a,b,c]
#         print(max(list)*100)

# lst = sorted(list(map(int, input().split())))

# if len(set(lst)) is 1:
#     print(10000 + lst[0]*1000)
# elif len(set(lst)) is 2:
#     print(1000 + lst[1]*100)  # pick middle
# else:
#     print(lst[2]*100)

a = int(input())
for _ in range(a):
    b = list(map(int, sys.stdin.readline().split()))
    avg = sum(b[1:])/b[0]
    c = [x for x in b if x>avg]
    print(f'{len(c)/len(b[1:])*100:.3f}%')
