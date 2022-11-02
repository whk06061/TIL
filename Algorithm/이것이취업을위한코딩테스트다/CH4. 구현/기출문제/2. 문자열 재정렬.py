import sys
sys.stdin = open("input.txt", "r")

s = input()
newS = ""
sumN = 0
for i in s:
    if i.isdecimal():
        sumN += int(i)
    else:
        newS += i
newS = ''.join(sorted(newS))
print(newS + str(sumN))