with open('_/input.txt', 'r') as file:
    lines = [int(x) for line in file for x in line.replace("\n", "").split(",")]
