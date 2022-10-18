import re

with open('17/input.txt', 'r') as file:
    line = [line.strip() for line in file][0]

    #target area: x=20..30, y=-10..-5
    result = re.search('target area: x=(.*)\.\.(.*), y=(.*)\.\.(.*)', line)
    x_min = int(result.group(1))
    x_max = int(result.group(2))
    y_min = int(result.group(3))
    y_max = int(result.group(4))

    target_area = [x_min, x_max, y_min, y_max]

    def in_target_area(target_area, coordinates):
        x, y = coordinates
        x_min, x_max, y_min, y_max = target_area
        return x_min <= x <= x_max and y_min <= y <= y_max

    def is_out(target_area, coordinates):
        x, y = coordinates
        _, x_max, y_min, _ = target_area
        return x > x_max or y < y_min

    def simulate(start, velocity, target_area):
        x_vel, y_vel = velocity
        position = start
        high_reached = y_vel == 0
        x_resistance = -1 if x_vel > -1 else 1
        max_y_position = -float("inf")
        while not is_out(target_area, position):
            x, y = position
            position = (x + x_vel, y + y_vel)
            x_vel = max(0, x_vel+x_resistance)
            y_vel = y_vel-1
            if position[1] > max_y_position:
                max_y_position = position[1]
            if in_target_area(target_area, position): return True, max_y_position
        return False, max_y_position

    
    max_y_position = -float("inf")
    valid_throws = 0
    for i in range(x_max+1): # brute force x_vel with upper limit of x_max
        for j in range(y_min-1, 2000): # brute force y_vel with lower limit of y_min
            in_area, max_y_position_ = simulate((0,0), (i,j), target_area)
            if in_area:
                valid_throws += 1
                if max_y_position_ > max_y_position:
                    max_y_position = max_y_position_

    print("Result 1:", max_y_position)
    print("Result 2:", valid_throws)
    

