
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

N = 10000
sosoo_list = []
for i in range(2, 10001):
    for j in range(2, int(i**0.5)+1):
        if i % j  == 0 :
            break
    else:
        sosoo_list.append(i)

input_n = int(input())
for _ in range(input_n):
    even_number = int(sys.stdin.readline())
    # 짝수를 반으로 나눈 값을 기준으로 함
    pivot = even_number // 2
    # 반으로 나눈 값이 소수라면 바로 정답 출력
    if pivot in sosoo_list:
        print(f'{pivot} {pivot}')
    # 아니라면 구해줘야 함
    else:
        while True:
            # pivot이 소수가 될 때 까지 1을 빼줌
            if pivot in sosoo_list:
                # pivot 말고 나머지 값도 소수라면 답 출력
                if (even_number - pivot) in sosoo_list:
                    print(f'{pivot} {even_number-pivot}')
                    break
                # 아니라면 pivot을 더 작은 소수로 바꿔줌
                else:
                    pivot_index = sosoo_list.index(pivot)
                    pivot = sosoo_list[pivot_index-1]
            else:
                pivot -= 1