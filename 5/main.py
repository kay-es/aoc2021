import math
import numpy as np

with open('5/input.txt', 'r') as file:
    lines = [line.strip().replace(" -> ", ",").split(",") for line in file]

coordinates = [[int(l)for l in line] for line in lines]

maximum_x = 0
maximum_y = 0
for l in coordinates:
    max_x = max(l[0], l[2])
    max_y = max(l[1], l[3])
    if max_x > maximum_x: maximum_x = max_x
    if max_y > maximum_y: maximum_y = max_y

# coordinates
coordinates_route = []
for c in coordinates:
    cs = []
    if c[0] == c[2]:
        minimum = min(c[3], c[1])
        for i in range(abs(c[3] - c[1]) + 1):
            cs.append([c[2], minimum + i])
        pass
    elif c[1] == c[3]:
        minimum = min(c[2], c[0])
        for i in range(abs(c[2] - c[0]) + 1):
            cs.append([minimum + i, c[1]])
    if cs != []:
        coordinates_route.append(cs)

diagram = [[0] * (maximum_x + 1) for _ in range(maximum_y + 1)]

for l in coordinates_route:
    for x in l:
        diagram[x[1]][x[0]] += 1

print("Result 1:", (np.asarray(diagram) >= 2).sum())

# coordinates
coordinates_route = []
for c in coordinates:
    x1, y1, x2, y2 = c
    cs = []
    
    if x1 == x2:
        minimum = min(y2, y1)
        for i in range(abs(y2 - y1) + 1):
            cs.append([x2, minimum + i])
    elif y1 == y2:
        minimum = min(x2, x1)
        for i in range(abs(x2 - x1) + 1):
            cs.append([minimum + i, y1])
    else:
        cs.extend([[int(x1 + x * math.copysign(1, x2 - x1)), int(y1 + x * math.copysign(1, y2 - y1))] for x in range(abs(x2 - x1) + 1)])
    if cs != []:
        coordinates_route.append(cs)
    

diagram = [[0] * (maximum_x + 1) for _ in range(maximum_y + 1)]

for l in coordinates_route:
    for x in l:
        diagram[x[1]][x[0]] += 1

print("Result 2:", (np.asarray(diagram) >= 2).sum())