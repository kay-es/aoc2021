from functools import reduce
import operator

def break_hierarchy(binary_code, hierarchy):
    version = int(binary_code[:3], base=2)
    packet_type_id = int(binary_code[3:6], base=2)
    length_type_id = int(binary_code[6:7], base=2)
    versions.append(version)

    leftover_bits = ""
    if length_type_id == 0:
        no_subpackets_length = 15
        no_subpackets = int(binary_code[7:7+no_subpackets_length], base=2)
        subpackets_bits = binary_code[7+no_subpackets_length:7+no_subpackets_length+no_subpackets]
        leftover_bits = binary_code[7+no_subpackets_length+no_subpackets:]
        subpackets_left = float("inf")
    else:
        no_subpackets_length = 11
        subpackets_left = int(binary_code[7:7+no_subpackets_length], base=2)
        subpackets_bits = binary_code[7+no_subpackets_length:]
    
    subpacket_values = []
    while(subpackets_left > 0 and len(subpackets_bits) > 0):
        subpacket_version = int(subpackets_bits[:3], base=2)
        subpacket_type_id = int(subpackets_bits[3:6], base=2)
        if subpacket_type_id == 4:
            subpackets_bits = subpackets_bits[6:]
            versions.append(subpacket_version)
            subpacket_value = ""
            while True:
                subpacket_part = subpackets_bits[:5]
                subpackets_bits = subpackets_bits[5:]
                subpacket_value += subpacket_part[1:]
                if subpacket_part.startswith("0"):
                    subpackets_left -= 1
                    break
            subpacket_values.append(int(subpacket_value, base=2))
        else:
            subpackets_left -= 1
            subpackets_bits, val = break_hierarchy(subpackets_bits, hierarchy+1)
            subpacket_values.append(val)
    if subpackets_left == 0: leftover_bits = subpackets_bits
    value = 0
    if packet_type_id == 0:
        value = sum(subpacket_values)
    elif packet_type_id == 1:
        value = reduce(operator.mul, subpacket_values, 1)
    elif packet_type_id == 2:
        value = min(subpacket_values)
    elif packet_type_id == 3:
        value = max(subpacket_values)
    elif packet_type_id == 5:
        value = 1 if subpacket_values[0] > subpacket_values[1] else 0
    elif packet_type_id == 6:
        value = 1 if subpacket_values[0] < subpacket_values[1] else 0
    elif packet_type_id == 7:
        value = 1 if subpacket_values[0] == subpacket_values[1] else 0
    return leftover_bits, value

if __name__ == "__main__":
    with open('16/input.txt', 'r') as file:
        packet = [line.strip() for line in file][0]
        versions = []
        binary_code = bin(int(packet, base=16))[2:].zfill(len(packet) * 4)

        _, value = break_hierarchy(binary_code, 0)

        print("Result 1:", sum(versions))
        print("Result 2:", value)