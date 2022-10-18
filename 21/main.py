with open('21/input.txt', 'r') as file:
    players = [int(line.strip()[-1]) for line in file]

    p1 = players[0]
    p2 = players[1]

    s1 = 0
    s2 = 0

    dice = 0
    turn_p1 = True
    round = 0
    while s1 < 1000 and s2 < 1000:
        round += 1
        dice += 3
        round_score = (dice * 3 -3) % 10
        if turn_p1:
            s = 10 if (p1 + round_score) % 10 == 0 else (p1 + round_score) % 10
            p1 = s
            s1 += s
            turn_p1 = False
        else:
            s = 10 if (p2 + round_score) % 10 == 0 else (p2 + round_score) % 10
            p2 = s
            s2 += s
            turn_p1 = True
        #print("Score:", s, dice, round_score)
    
    print(dice)
    print(s1, s2)
    print(dice * min(s1, s2))
