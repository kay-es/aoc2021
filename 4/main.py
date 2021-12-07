with open('4/input.txt', 'r') as file:
    lines = [line.replace("\n", "") for line in file]

# gen numbers to draw
numbers = [int(l) for l in lines[0].split(",")]

# gen boards
boards = []
board = []
for l in lines[2:]:
    if len(l) > 0:
        board.append([int(x) for x in l.split()])
    else:
        boards.append(board)
        board = []
boards.append(board)

def play_bingo(boards, numbers):
    numbers_drawn = []
    for n in numbers:
        numbers_drawn.append(n)
        for b in boards:
            # check rows
            for row in b:
                if len(numbers_drawn) >= len(row):
                    if all(x in numbers_drawn for x in row):
                        return b, n, numbers_drawn
            # check cols
            for col in zip(*b):
                if len(numbers_drawn) >= len(col):
                    if all(x in numbers_drawn for x in col):
                        return b, n, numbers_drawn

def play_bingo_finish_last(boards, numbers):
    numbers_drawn = []
    boards_leftovers = boards
    for n in numbers:
        numbers_drawn.append(n)
        for b in boards:
            # check rows
            for row in b:
                if len(numbers_drawn) >= len(row):
                    if all(x in numbers_drawn for x in row):
                        if len(boards_leftovers) == 1:
                            return b, n, numbers_drawn
                        else:
                            if b in boards_leftovers: boards_leftovers.remove(b)
                            break
            # check cols
            for col in zip(*b):
                if len(numbers_drawn) >= len(col):
                    if all(x in numbers_drawn for x in col):
                        if len(boards_leftovers) == 1:
                            return b, n, numbers_drawn
                        else:
                            if b in boards_leftovers: boards_leftovers.remove(b)
                            break


if __name__ == "__main__":
    b, n, numbers_drawn = play_bingo(boards=boards, numbers=numbers)
    print("Result 1:", sum([x for row in b for x in row if x not in numbers_drawn]) * n)


    b, n, numbers_drawn = play_bingo_finish_last(boards=boards, numbers=numbers)
    print("Result 2:", sum([x for row in b for x in row if x not in numbers_drawn]) * n)
    
    
