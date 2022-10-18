import itertools

def filter(image, image_algo, steps):
    residual_image_pixels = []
    for step in range(steps):
        ver = len(image)
        hor = len(image[0])

        v_offsets = [-1, -1, -1,  0, 0,  0, +1, +1, +1]
        h_offsets = [-1,  0, +1, -1, 0, +1, -1,  0, +1]

        residual_image_pixels = [[] for _ in range(ver+2)]
        ver_residual = hor_residual = len(residual_image_pixels)
        residual_image = []
        for i in range(-1, ver+1):
            residual_image_part = []
            for j in range(-1, hor+1):
                bin_pixels = ""
                for v_offset, h_offset in zip(v_offsets, h_offsets):
                    i_offset = i + v_offset
                    j_offset = j + h_offset
                    if 0 <= i_offset < ver and 0 <= j_offset < hor:
                        if image[i_offset][j_offset] == "#":
                            bin_pixels += "1"
                        else:
                            bin_pixels += "0" 
                    else:
                        bin_pixels += "1" if image_algo[0] == "#" and step % 2 == 1 else "0"
                x = int(bin_pixels, base=2)
                residual_image_part.append(x)
            residual_image.append(residual_image_part)


        for i in range(ver_residual):
            for j in range(hor_residual):
                residual_image_pixels[i].append(image_algo[residual_image[i][j]])

        image = residual_image_pixels
    
    return sum([line.count("#") for line in residual_image_pixels])


if __name__ == "__main__":
    with open('20/input.txt', 'r') as file:
        image_algo = "".join([x.strip() for x in list(itertools.takewhile(lambda x: x != "\n", file))])
        image = [list(rule.strip()) for rule in file]
    
        print("Result 1:", filter(image, image_algo, 2))
        print("Result 2:", filter(image, image_algo, 50))

