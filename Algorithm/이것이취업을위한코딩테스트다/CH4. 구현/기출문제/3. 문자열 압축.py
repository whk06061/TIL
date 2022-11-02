import sys
sys.stdin = open("input.txt", "r")
s = input()
answer = 1247000000

for i in range(1, len(s)+1):
    result = ""
    unit = i
    previous = s[0: unit]
    count = 1
    for j in range(unit, len(s), unit):
        if s[j: j+unit] == previous:
            count += 1
        else:
            result += (str(count) + previous) if count > 1 else previous
            previous = s[j: j+unit]
            count = 1
    result += (str(count) + previous) if count > 1 else previous
    answer = min(answer, len(result))
print(answer)
