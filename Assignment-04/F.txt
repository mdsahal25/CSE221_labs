N = int(input())
x, y= (map(int, input().split()))
directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
moves = []
for dx, dy in directions:
        nx = x + dx
        ny = y + dy
        if 1 <= nx <= N and 1 <= ny <= N:
            moves.append((nx, ny))
moves.sort()
print(len(moves))
for move in moves:
    print(move[0], move[1])