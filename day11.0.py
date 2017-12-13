with open("day11.txt", "r") as fin:
	data = fin.read().strip().split(',')

ops = {'n': (-1, -1), 'nw': (0, -1), 'sw': (1, 0), 's': (1, 1), 'se': (0, 1), 'ne': (-1, 0)}

x, y = 0, 0
for op in data:
	x += ops[op][0]
	y += ops[op][1]

print max(abs(x), abs(y))
