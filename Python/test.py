
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

N = 123456
sosoo_list = [False] * (N*2+1)
# 2 * N 까지의 모든 소수 구하기
for i in range(2,N*2+1):
    for j in range(2, int(i**0.5)+1):
        if i % j == 0:
            break
    else:
        sosoo_list[i] = True

# 입력받은 수 범위에서 소수 개수 구하기
while True:
    result = 0
    input_n = int(input())
    if input_n == 0:
        break
    for i in range(input_n+1, 2*input_n+1):
        if sosoo_list[i] == True:
            result += 1
    print(result)