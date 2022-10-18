
with open('2/input.txt', 'r') as file:
    lines = [line.strip().split(" ") for line in file]

    forwards = [int(l[1]) for l in lines if l[0] == "forward"]
    ups = [int(l[1]) for l in lines if l[0] == "up"]
    downs = [int(l[1]) for l in lines if l[0] == "down"]

    print("Result 1:", sum(forwards) * (sum(downs) - sum(ups)))


    aim = 0
    depth = 0
    horizontal = 0
    for l in lines:
        summand = int(l[1])
        if l[0] == "forward":
            horizontal += summand
            depth += aim * summand
        elif l[0] == "up":
            aim -= summand
        elif l[0] == "down":
            aim += summand

    print("Result 2:", horizontal * depth)