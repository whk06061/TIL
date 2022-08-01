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



def find_keys(dict, val):
    return list(key for key, value in dict.items() if value == val)

a = input().upper()
result = {}
for i in a:
    if i in result:
        result[i] += 1
    else: result[i] = 1
max_value = max(result.values())
key_list = find_keys(result, max_value)
if len(key_list) == 1:
    print(key_list[0])
else:
    print("?")