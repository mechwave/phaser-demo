import random
from ...tools.map_utils import MapTile, Tile

random.seed(version=2)
MAX_X = 70
MAX_Y = 70
CLUSTERING_PROBALITY_COEFFICIENT = 0.7
START_CLUSTERING_TILES_COUNT = 2


def change_terrain_value(value):
    """Changes terrain value."""
    if value == "GROUND":
        return "SAND"
    if value == "SAND":
        return "GROUND"
    return 0

def clustering_neighbors(array, x, y):
    """Tiles clusterization."""
    counter = 0
    value = array[x][y]
    tile = Tile(x, y)
    neighbors = tile.neighbors()
    for item in neighbors:
        if item.x < MAX_X and item.y < MAX_Y:
            if array[item.x][item.y] == value:
                counter = counter + 1
    if counter > START_CLUSTERING_TILES_COUNT:
        if random.random() > CLUSTERING_PROBALITY_COEFFICIENT:
            for item in neighbors:
                if item.x < MAX_X and item.y < MAX_Y:
                    array[item.x][item.y] = value

def change_tile_type(array, x, y):
    """Change type if neighboring tiles has a certain amount of other tile type."""
    counter = 0
    value = array[x][y]
    tile = Tile(x, y)
    neighbors = tile.neighbors()
    for item in neighbors:
        if item.x < MAX_X and item.y < MAX_Y and array[item.x][item.y] == value:
            counter = counter +1
    if counter < 5:
        array[x][y] = change_terrain_value(value)
        
def seed(width,height):
    """Generate tilemap."""
    array = [[0 for x in range(width)] for y in range(height)]
    #seed
    for x in range(width):
        for y in range(height):
            value = random.random()
            if value > 0.5:
                array[x][y] = 'GROUND'
            else:
                array[x][y] = 'SAND'
            #array[x][y] = random.random()
    #clusterization
    for x in range(width):
        for y in range(height):
            clustering_neighbors(array,x,y)
    #changing type of single terrain tiles 
    for x in range(width):
        for y in range(height):
            change_tile_type(array,x,y)
    return array

def get_random_map():
    """Get random map."""
    random.seed(version=2)
    width, height = MAX_X, MAX_Y
    terrain = seed(width, height)
    array = []
    #array = [[Tile(x,y) for x in range(w)] for y in range(h)]
    for x in range(width):
        for y in range(height):
            array.append(MapTile(x,y, terrain[x][y]))
    return array, MAX_X, MAX_Y
