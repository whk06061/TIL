height_list = []
one = 0
two = 0
is_break = False

for _ in range(9):
    height_list.append(int(input()))

for i in range(0, 8):
    for j in range(i+1, 9):
        if height_list[i] + height_list[j] == sum(height_list) - 100:
            one = height_list[i]
            two = height_list[j]
            is_break = True
            break
    if is_break:
        break
height_list.remove(one)
height_list.remove(two)
height_list.sort()
print(height_list)