
with open('1/input.txt', 'r') as file:
    lines = [int(line.rstrip()) for line in file]

cnt = 0
for i in range(len(lines) - 1):
    if lines[i] < lines[i+1]:
        cnt += 1

print("Result 1", cnt)

cnt = 0
for i in range(len(lines) - 3):
    if sum(lines[i:i+3]) < sum(lines[i+1:i+4]):
        cnt += 1

print("Result 2", cnt)