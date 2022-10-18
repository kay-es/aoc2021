with open('11/input.txt', 'r') as file:
    octs = [list(map(lambda x: int(x), list(line.strip()))) for line in file]

ver = len(octs)
hor = len(octs[0])

v_offsets = [1, 1, 0, -1, -1, -1,  0,  1]
h_offsets = [0, 1, 1,  1,  0, -1, -1, -1]

flashes = 0
processed = set()
cnt = 0
while True:
    if len(processed) == 100:
        break
    if cnt == 100:
        print("Result 1:", flashes)
    cnt += 1
    processed.clear()
    flashed = []
    for i in range(ver):
        for j in range(hor):
            octs[i][j] += 1
            if octs[i][j] > 9:
                octs[i][j] = 0
                flashes += 1
                processed.add((i, j))
                flashed.append([i, j])

    while flashed:
        i, j = flashed.pop()
        for v_offset, h_offset in zip(h_offsets, v_offsets):
            i_offset = i + v_offset
            j_offset = j + h_offset
            if 0 <= i_offset < ver and 0 <= j_offset < hor and not (i_offset, j_offset) in processed:
                octs[i_offset][j_offset] += 1
                if octs[i_offset][j_offset] > 9:
                    octs[i_offset][j_offset] = 0
                    flashes += 1
                    processed.add((i_offset, j_offset))
                    flashed.append([i_offset, j_offset])

print("Result 2:", cnt)