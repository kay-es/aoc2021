with open('8/input.txt', 'r') as file:
    lines = [line.strip().split(" | ") for line in file]
    patterns = [sorted(line[0].split(" "), key=len) for line in lines]
    outputs = [line[1].split(" ") for line in lines]

print("Result 1:", sum([len([x for x in o if len(x) in [2, 3, 4, 7]]) for o in outputs]))

cnt = 0
for pattern, o in zip(patterns, outputs):
    pattern = ["".join(sorted(p)) for p in pattern]
    one = pattern[0]
    four = pattern[2]
    seven = pattern[1]
    eight = pattern[9]
    mapping = {
        one: "1",
        four: "4",
        seven: "7",
        eight: "8"
    }
    for p in pattern:
        if len(p) == 5:
            if len(set(p).intersection(one)) == 2:
                mapping[p] = "3"
            elif len(set(p).intersection(four)) == 2:
                mapping[p] = "2"
            else:
                mapping[p] = "5"
        elif len(p) == 6:
            if len(set(p).intersection(one)) == 2:
                if len(set(p).intersection(four)) == 3:
                    mapping[p] = "0"
                else:
                    mapping[p] = "9"
            else:
                mapping[p] = "6"

    sent_number = ""
    for x in o:
        sent_number += mapping["".join(sorted(x))]
    cnt += int(sent_number)

print("Result 2:", cnt)