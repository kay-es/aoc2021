import itertools
import collections

with open('13/input.txt', 'r') as file:
    lines = list(itertools.takewhile(lambda x: x != "\n", file))
    tags = [list(map(lambda x: int(x), line.strip().split(","))) for line in lines]

    folds = []
    for fold in file:
        fold_coord = fold[11:].strip()
        ax, dim = fold_coord.split("=")
        folds.append([ax, int(dim)])

    cols = max([x[0] for x in tags]) + 1
    rows = max([y[1] for y in tags]) + 1
    rows = rows if rows % 2 == 1 else rows + 1

paper = [[" " for _ in range(cols)] for _ in range(rows)]
for j, i in tags:
    paper[i][j] = "█"

cnt = 0
folded_paper = paper

for i, (ax, dim) in enumerate(folds):
    if i == 1:
        for row in folded_paper:
            cnt += collections.Counter(row)["█"]
        print("Result 1:", cnt)
    folding_rows = []
    if ax == "y":
        for a, b in zip(folded_paper[:dim], reversed(folded_paper[dim+1:])):
            folding_rows.append(["█" if cell_a == "█" or cell_b == "█" else " " for cell_a, cell_b in zip(a, b)])
    else:
        for row in folded_paper:
            folding_rows.append(["█" if cell_a == "█" or cell_b == "█" else " " for cell_a, cell_b in zip(row[:dim], reversed(row[dim+1:]))])
    folded_paper = folding_rows
        
print("Result 2:")
for l in folded_paper:
    print("".join(l))