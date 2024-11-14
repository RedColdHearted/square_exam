from square import Square

class SquareRepository:
    """Repository with instance managing methods for `Square`."""
    def __init__(self):
        self.data = {}
        self.index = 0

    def add(self, square: Square) -> None:
        """Add and return `Square` instance."""
        self.index += 1
        self.data[self.index] = square
        return square

    def remove(self, index: int) -> None:
        """Remove `Square` instance and return index."""
        del self.data[index]
        return index

    def get(self, index: int) -> Square:
        """Return `Square` instance."""
        return self.data[index]

    def get_all(self) -> dict[int: Square]:
        """Return all `Square` instances."""
        return self.data