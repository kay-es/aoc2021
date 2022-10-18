with open('input.txt', 'r') as file:
    lines = [line.strip() for line in file]

point_mapping = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}

openings = "([{<"
closings = ")]}>"

points = 0
total_scores = []
for l in lines:
    subscore = 0
    s = []
    for c in l:
        if c in openings:
            s.append(closings[openings.index(c)])
        elif s.pop() != c:
            points += point_mapping[c]
            break
    else:
        for c in reversed(s):
            subscore = subscore * 5 + (closings.index(c) + 1)
        total_scores.append(subscore)
          
print("Result 1:", points)
print("Result 2:", sorted(total_scores)[len(total_scores) // 2])

