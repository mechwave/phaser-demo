import os
import uuid
import datetime
import random

from pyrsistent import v
from ...tools.map_utils import MapTile, Tile

random.seed(version=2)
max_x = 20
max_y = 20
def clustering_neighbors(array, x, y):
    # 0.75 3
    CLUSTERING_PROBALITY_COEFFICIENT = 0.75
    START_CLUSTERING_TILES_COUNT = 4
    counter = 0
    value = array[x][y]
    tile = Tile(x, y)
    neighbors = tile.neighbors()
    for item in neighbors:
        if item.x < max_x and item.y < max_y:
            if array[item.x][item.y] == value:
                counter = counter + 1
    #if counter > START_CLUSTERING_TILES_COUNT:
    if random.random() > CLUSTERING_PROBALITY_COEFFICIENT:
        for item in neighbors:
            if item.x < max_x and item.y < max_y:
                array[item.x][item.y] = value


def noise(w,h):
    array = [[0 for x in range(w)] for y in range(h)]
    #seed
    for x in range(w):
        for y in range(h):
            value = random.random()
            if value > 0.6:
                array[x][y] = 'GROUND'
            else:
                array[x][y] = 'SAND'
            #array[x][y] = random.random()
    #clusterization
        for x in range(w):
            for y in range(h):
                clustering_neighbors(array,x,y)
    return array

def get_random_map():
    """Get random map."""
    random.seed(version=2)
    w, h = max_x, max_y
    terrain = noise(w,h)
    array = []
    #array = [[Tile(x,y) for x in range(w)] for y in range(h)]
    for x in range(w):
        for y in range(h):
            array.append(MapTile(x,y, terrain[x][y]))
    return array