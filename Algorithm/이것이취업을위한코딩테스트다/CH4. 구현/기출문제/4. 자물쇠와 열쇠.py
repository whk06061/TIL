import sys
sys.stdin = open("input.txt", "r")

key = [[0, 1, 0], [1, 0, 0], [1, 0, 0]]
new_key = []
print([[0] + row[0:len(key)-1]  for row in key])
for row in key:
    new_key.append([0]+row[0:len(key)-1])