
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

    def __init__(self, x, y, empty, hit):
        self.x = x
        self.y = y
        self.line = [empty] * x
        self.hit = hit

    def get_field(self):
        return self.field

    def draw_field(self):

        for i in range(self.y):
            self.field.append(self.line)

        return self.field

    def update_field(self, x: str, y):
        try:
            a_coord = dictionary[x]
            b_coord = int(y) - 1
        except Exception as e:
            print(e)
            pass
        self.field[a_coord][b_coord] = self.hit
        print(self.field[a_coord][b_coord])
        print(self.field[a_coord][b_coord+1])
        print(self.field[a_coord])
        print(self.field[a_coord + 1])


class Game:
    """
    Main class that controls the game
    """
    game_status = 0

    def __init__(self, x: int, y: int, empty: str, hit: str):
        self.x = x
        self.y = y
        self.empty = empty
        self.hit = hit

        self.field = Field(x, y, empty, hit)
        self.current_field = self.initialize_field()

    def initialize_field(self):

        field = self.field.draw_field()
        text = ""
        for i in field:
            for j in i:
                text += f"{j} "
            text += "\n"
        return text

    def update_field(self, x, y):
        self.field.update_field(x, y)
        self.field.get_field()

    def draw_field

if __name__ == '__main__':
    game = Game(10, 10, "0", "*")
    game.update_field("A", 1)
