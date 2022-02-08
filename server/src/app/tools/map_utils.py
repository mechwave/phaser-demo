"""Map utils."""

class Tile:
    """Tile base class."""

    x: int
    y: int
    w: int
    h: int

    def __init__(self, x: int, y: int, w = 1, h = 1):
        """Init."""
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def sum(self, tile: 'Tile'):
        """Scalar sum of two tiles."""
        if (self.x + tile.x >= 0) and (self.y + tile.y >= 0):
            return Tile(x = self.x + tile.x, y = self.y + tile.y)
        else:
            return None

    def neighbors(self):
        """Return tiles array around the current tile."""
        #return [self.sum(x) for x in NEIGHBORS]
        array = []
        for item in NEIGHBORS:
            if self.sum(item):
                array.append(self.sum(item))
        return array

    def path_to(self, tile: 'Tile'):
        """Return tiles array represents path to target tile."""
        return None

NEIGHBORS = [Tile(x = 0, y = 1),
            Tile(x = 1, y = 1),
            Tile(x = 1, y = 0),
            Tile(x = 1, y = -1),
            Tile(x = 0, y = -1),
            Tile(x = -1, y = -1),
            Tile(x = -1, y = 0),
            Tile(x = -1, y = 1)]

class MapTile(Tile):
    terrain: str
 
    def __init__(self, x: int, y: int, terrain: str):
        """Init."""
        self.x = x
        self.y = y
        self.terrain = terrain

    def set_terrain(self, terrain:str):
        self.terrain = terrain