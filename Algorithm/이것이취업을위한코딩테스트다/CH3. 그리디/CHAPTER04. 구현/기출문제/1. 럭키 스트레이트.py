import sys

sys.stdin = open("input.txt", "r")

n = input()
size = len(n)
n1 = list(map(int, n[0: (size // 2)]))
n2 = list(map(int, n[size // 2:]))
if sum(n1) == sum(n2):
    print("LUCKY")
else:
    print("READY")
