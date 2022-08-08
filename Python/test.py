
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

# 생성자 없는 수 구하기
# a = [x for x in range(0,10001)]
# for i in range(0,10001):
#     result = i
#     for j in str(i):
#         result += int(j)
#     if result in a:
#         a.remove(result)
# print(*a, sep="\n")

#한수 개수 구하기
# a = input()
# result = []
# for i in range(97, 123):
#     if chr(i) in a:
#         result.append(a.index(chr(i)))
#     else:
#         result.append(-1)
# print(*result, sep=" ")

import sys
a = int(sys.stdin.readline())
for _ in range(a):
    k = int(sys.stdin.readline())
    n = int(sys.stdin.readline())
    f0 = [x for x in range(1, n+1)]
    for i in range(k):
        for j in range(1, n):
            f0[j] += f0[j-1]
    print(f0[-1])
