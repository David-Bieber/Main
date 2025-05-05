import numpy as np
import matplotlib.pyplot as plt
import random

class chunk_object:
    def __init__(self, pos_x, pos_y, pos_z, s_x = 1, s_y = 1, s_z = 1):
        self.size = [s_x, s_y, s_z]
        self.pos = [pos_x, pos_y, pos_z]

    


def create_grid(x, y, z = 1):
    # used to create a grid as base for the world
    grid = [[[chunk_object(x_, y_, z_, ) for z_ in range(z)] for y_ in range(y)] for x_ in range(x)]
    
    for i in grid:
        for j in i:
            for k in j:
                print(f'pos: {k.pos} size: {k.size}')

    return grid



# print(create_grid(10, 10))

create_grid(5, 5, 5)

plt.imshow(create_grid(10, 10))