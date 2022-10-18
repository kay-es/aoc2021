import collections

with open('6/input.txt', 'r') as file:
    lines = [int(x) for line in file for x in line.strip().split(",")]

cnts = collections.Counter(lines)
max_recreation = max(9, max(lines)) + 1

def get_sum_of_fishes(days):
    for _ in range(days):
        recreations = cnts[0]
        for i in range(1, max_recreation):
            cnts[i-1] = cnts[i]
        cnts[6] += recreations
        cnts[8] += recreations
    return sum(cnts.values())

if __name__ == "__main__":
    
    print("Result 1:", get_sum_of_fishes(80))
    print("Result 2:", get_sum_of_fishes(256))



"""
# TRIVIAL VERSION FOR PART 1 WITH HIGH RUNTIME
recreation_time = 7
fish_gens = [lines]
for d in range(1, 1+256):
    for i, fish_gen in enumerate(fish_gens):
        for j in range(len(fish_gen)):
            fish_gens[i][j] -= 1
            fish = fish_gens[i][j]

            if fish == -1:
                fish_gens[i][j] = recreation_time - 1
                if len(fish_gens) == i+1:
                    fish_gens.append([])
                fish_gens[i+1].append(recreation_time + 2)
"""