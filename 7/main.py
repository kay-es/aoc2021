with open('7/input.txt', 'r') as file:
    lines = [int(x) for line in file for x in line.replace("\n", "").split(",")]

hmin = min(lines)
hmax = max(lines)

def get_position_with_minimum_fuel(sum_function):
    best_pos = -1
    best_fuel = float("inf")
    for x in range(hmin, hmax):
        fuel = int(sum([sum_function(x, p) for p in lines]))
        if fuel < best_fuel:
            best_pos = x
            best_fuel = fuel

    return best_fuel, best_pos

if __name__ == "__main__":

    best_fuel, best_pos = get_position_with_minimum_fuel(lambda x, p: abs(p - x))
    print("Result 1:", best_fuel, "\t- Best Position:", best_pos)
    
    best_fuel, best_pos = get_position_with_minimum_fuel(lambda x, p: (abs(p - x)**2 + abs(p - x)) / 2)
    print("Result 2:", best_fuel, "\t- Best Position:", best_pos)