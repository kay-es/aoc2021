from functools import reduce
import operator

with open('9/input.txt', 'r') as file:
    lines = [list(map(lambda x: int(x), list(line.strip()))) for line in file]

ver = len(lines)
hor = len(lines[0])

v_offsets = [-1, 0, 1,  0]
h_offsets = [ 0, 1, 0, -1]

potentials = []
for i in range(ver):
    for j in range(hor):
        potential = lines[i][j]
        add = True
        for v_offset, h_offset in zip(v_offsets, h_offsets):
            i_offset = i + v_offset
            j_offset = j + h_offset
            
            if 0 <= i_offset < ver and 0 <= j_offset < hor and potential >= lines[i_offset][j_offset]:
                add = False
                break
        if add: potentials.append(potential)

print("Result 1:", sum(potentials) + len(potentials))


seen = []
basins = []

def find_basins(i, j):
    if [i, j] in seen:
        return []
    seen.append([i, j])
    b = [[i,j]]

    for v_offset, h_offset in zip(v_offsets, h_offsets):
        i_offset = i + v_offset
        j_offset = j + h_offset

        if 0 <= i_offset < ver and 0 <= j_offset < hor and lines[i_offset][j_offset] != 9:
            b.extend(find_basins(i_offset, j_offset))
    return b

for i in range(ver):
    for j in range(hor):
        if lines[i][j] != 9:
            basin = find_basins(i, j)
            basins.append(basin)

biggest_basins = sorted([len(b) for b in basins])[-3:]
print("Result 2:", reduce(operator.mul, biggest_basins, 1))