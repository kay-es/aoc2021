with open('3/input.txt', 'r') as file:
    lines = [list(line.strip()) for line in file]

lines_trans = list(zip(*lines))
gamma_rate = ""
epsilon_rate = ""

for col in lines_trans:
    gamma_rate += max(col, key = col.count)
    epsilon_rate += min(col, key = col.count)

gamma_rate = int(gamma_rate, 2)
epsilon_rate = int(epsilon_rate, 2)
print("Result 1:", gamma_rate * epsilon_rate)

oxygen_list = lines
co2_list = lines

for i in range(len(lines_trans)):
    oxygen_list_trans = list(zip(*oxygen_list))
    co2_list_trans = list(zip(*co2_list))

    oxy_val = "1" if max(oxygen_list_trans[i], key = oxygen_list_trans[i].count) == min(oxygen_list_trans[i], key = oxygen_list_trans[i].count) else max(oxygen_list_trans[i], key = oxygen_list_trans[i].count)
    co2_val = "0" if max(co2_list_trans[i], key = co2_list_trans[i].count) == min(co2_list_trans[i], key = co2_list_trans[i].count) else min(co2_list_trans[i], key = co2_list_trans[i].count)
    
    if len(oxygen_list) > 1:
        indices_oxygen = []
        for l in oxygen_list:
            if l[i] == oxy_val:
                indices_oxygen.append(l)
        oxygen_list = indices_oxygen

    if len(co2_list) > 1:
        indices_co2 = []
        for l in co2_list:
            if l[i] == co2_val:
                indices_co2.append(l)
        co2_list = indices_co2


oxygen_rating = int("".join(oxygen_list[0]), 2)
co2_rating = int("".join(co2_list[0]), 2)
print("Result 2:", oxygen_rating * co2_rating)