"""Map utils."""

class Tile:
    """Tile base class."""

    x_coord: int
    y_coord: int
    x_size: int
    y_size: int

    def __init__(self, x_coord: int, y_coord: int, x_size = 1, y_size = 1):
        """Init."""
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.x_size = x_size
        self.y_size = y_size

    def sum(self, tile: 'Tile'):
        """Scalar sum of two tiles."""
        return Tile(x_coord = self.x_coord + tile.x_coord, y_coord = self.y_coord + tile.y_coord)

    def neighbors(self):
        """Return tiles array around the current tile."""
        return [self.sum(x) for x in NEIGHBORS]

    def path_to(self, tile: 'Tile'):
        """Return tiles array represents path to target tile."""
        return None

NEIGHBORS = [Tile(x_coord = 0, y_coord = 1),
            Tile(x_coord = 1, y_coord = 1),
            Tile(x_coord = 1, y_coord = 0),
            Tile(x_coord = 1, y_coord = -1),
            Tile(x_coord = 0, y_coord = -1),
            Tile(x_coord = -1, y_coord = -1),
            Tile(x_coord = -1, y_coord = 0),
            Tile(x_coord = -1, y_coord = 1)]
