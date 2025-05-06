import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import random
from collections import defaultdict

class chunk_object:
    def __init__(self, pos_x, pos_y, pos_z, s_x = 1, s_y = 1, s_z = 1):
        self.size = [s_x, s_y, s_z]
        self.pos = [pos_x, pos_y, pos_z]
        self.ident = (f'{pos_x}-{pos_y}-{pos_z}')
    


def create_grid(x, y, z = 1):

    # creating base grid

    grid = {}
    
    for x_ in range(x):
        for y_ in range(y):
            for z_ in range(z):

                #print(f'pos: {x_},{y_},{z_}')
                chunk = chunk_object(x_, y_, z_)
                ident = (f'{x_}-{y_}-{z_}')
                grid[ident] = chunk


    return grid

def render_chunk_object(chunk: chunk_object):
    chunk_pos = chunk.pos
    chunk_size = chunk.size
    fig = plt.figure()
    ax = fig.add_subplot((chunk_size[0],chunk_size[1],chunk_size[2]), projection='3d')



# print(create_grid(10, 10))

grid = create_grid(3, 3, 3)

for i in grid:
    # position output
    print(f'position: {grid[i].pos} size: {grid[i].size}')
