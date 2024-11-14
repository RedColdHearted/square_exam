from square import Square

class SquareRepository:
    def __init__(self):
        self.data = {}
        self.index = 0

    def add(self, square: Square) -> None:
        self.index += 1
        self.data[self.index] = square
        return square

    def remove(self, index: int) -> None:
        del self.data[index]
        return index

    def get(self, index: int) -> Square:
        return self.data[index]

    def get_all(self) -> dict[int: Square]:
        return self.data