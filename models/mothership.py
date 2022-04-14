
class Ship:
    parts: int = 0
    parts_hit: int = 0
    active: bool = True

    def __init__(self, parts: int):
        self.parts = parts

    def get_hit(self, coordinates: tuple):
        pass

    def __str__(self):
        text = f"This is a {self.parts} parted ship, currently has {self.parts_hit} parts hit"
