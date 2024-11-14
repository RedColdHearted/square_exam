class Square:
    """Represent a square with coordinates of top left angel
    and side length in centimeters.
    """

    def __init__(self, x: int, y: int, side_length: float ):
        self.x = x
        self.y = y
        self.side_length = side_length

    def get_area(self) -> float:
        """Return area."""
        return self.side_length ** 2

    def get_perimeter(self) -> float:
        """Return perimeter."""
        return self.side_length * 4