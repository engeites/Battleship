import os

dictionary = {
    "A": 0,
    "B": 1,
    "C": 2,
    "D": 3,
    "E": 4,
    "F": 5,
    "G": 6,
    "H": 7,
    "I": 8,
    "J": 9
}


class Field:
    field = []

    def __init__(self, x: int, y: int, empty: str = "0", hit: str = "*"):
        self.x = y  # horizontal length
        self.y = y  # vertical length
        self.empty = empty  # empty sign to draw with
        self.hit = hit  # look of cell when hit
        self.line = [empty] * x  # drawn initial line

    def create_field(self):
        for i in range(self.y):
            self.field.append(self.line.copy())

    def get_field(self):
        field_drawn = ""

        for line in self.field:
            for char in line:
                field_drawn += f"{char} "
            field_drawn += "\n"
        return field_drawn

    def update_field(self, hor, vert):
        x = dictionary[hor]
        y = int(vert) - 1
        self.field[x][y] = self.hit



if __name__ == '__main__':
    a = input("HELLO THERE!")
    field = Field(10, 10)
    field.create_field()
    current_field = field.get_field()
    print(current_field)
    coordinatex = input("ABCDEFGHIG")
    coordinatey = input("123456789")
    field.update_field(coordinatex, coordinatey)
    current_field = field.get_field()
    print(current_field)