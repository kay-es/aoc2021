from typing import List

import networkx as nx
import numpy as np

def find_shortest_length(lines: List[List[int]], factor: int):
    """
    PREPARE MAP
    """
    lines = np.array(lines)
    # vertically stacking
    manipulate_map = lambda x: (x+i) if (x+i) < 10 else (x+i) % 10 + 1
    lines_to_stack = lines
    for i in range(1, factor):
        lines = np.vstack((lines, np.array([list(map(manipulate_map, line)) for line in lines_to_stack])))
    # horizontally stacking
    lines_to_stack = lines
    for i in range(1, factor):
        lines = np.hstack((lines, np.array([list(map(manipulate_map, line)) for line in lines_to_stack])))

    """
    CALC
    """
    G = nx.DiGraph()

    ver = len(lines)
    hor = len(lines[0])

    v_offsets = [-1, 0, 1,  0]
    h_offsets = [ 0, 1, 0, -1]

    for i in range(ver):
        for j in range(hor):
            for v_offset, h_offset in zip(v_offsets, h_offsets):
                i_offset = i + v_offset
                j_offset = j + h_offset
                
                if 0 <= i_offset < ver and 0 <= j_offset < hor:
                    G.add_edge((i, j), (i_offset, j_offset), weight=lines[i_offset][j_offset])

    start, end = (0, 0), (ver-1, hor-1)
    risk = nx.shortest_path_length(G, start, end, weight="weight")
    return risk

if __name__ == "__main__":

    with open('15/input.txt', 'r') as file:
        lines = [list(map(lambda x: int(x), list(line.strip()))) for line in file]
        print("Result 1:", find_shortest_length(lines, 1))
        print("Result 2:", find_shortest_length(lines, 5))
                
