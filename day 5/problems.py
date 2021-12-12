from util import read_into, x1, x2, y1, y2

lines = []
read_into(lines, 'input.txt')

def is_diagonal(line):
    return x2(line) - x1(line) == abs(y2(line) - y1(line))

horizontal_lines = list(filter(lambda line : y1(line) == y2(line), lines))
vertical_lines = list(filter(lambda line : x1(line) == x2(line), lines))
diagonal_lines = list(filter(lambda line : is_diagonal(line), lines))

grid = [[0 for y in range(1000)] for x in range(1000)]

def get_points(line):
    if x1(line) == x2(line):
        return [(x1(line), y) for y in range(y1(line), y2(line) + 1)]
    elif y1(line) == y2(line):
        return [(x, y1(line)) for x in range(x1(line), x2(line) + 1)]
    elif y1(line) < y2(line):
        return [(x1(line) + i, y1(line) + i) for i in range(x2(line) - x1(line) + 1)]
    else:
        return [(x1(line) + i, y1(line) - i) for i in range(x2(line) - x1(line) + 1)]

points = {}

def mark_point(p):
    if p in points:
        points[p] += 1
    else:
        points[p] = 1

for line in horizontal_lines + vertical_lines:
    line_points = get_points(line)
    for point in line_points:
        mark_point(point)

count = 0
for val in points.values():
    if val >= 2:
        count += 1

print(count) # problem 1 answer is 6267

for line in diagonal_lines:
    line_points = get_points(line)
    for point in line_points:
        mark_point(point)

count = 0
for val in points.values():
    if val >= 2:
        count += 1

print(count)