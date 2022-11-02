import sys

sys.stdin = open("input.txt", "r")
n, m = map(int, input().split())
x, y, direction = map(int, input().split())
# 전체 맵 정보 저장
maps = [list(map(int, input().split())) for _ in range(n)]
# 방문한 위치 저장
d = [[0] * m for _ in range(n)]
d[x][y] = 1

# 북, 동, 남, 서 정의
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


# 왼쪽 으로 회전
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3


# 시뮬레이션 시작
count = 1
turn_time = 0
while True:
    # 왼쪽으로 회전
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    if d[nx][ny] == 0 and maps[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        turn_time = 0
        count += 1
        continue
    else:
        turn_time += 1
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        if maps[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        turn_time = 0

print(count)
