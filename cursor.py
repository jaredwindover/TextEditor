class Cursor:
    def __init__(self):
        self.x = 0
        self.y = 0

    def __str__(self):
        return "({},{})".format(self.x, self.y)

    def MoveLeft(self, contents):
        self.x = max(0, min(self.x - 1, len(contents[self.y]) - 1))

    def MoveRight(self, contents):
        self.x = max(0, min(len(contents[self.y]) - 1, self.x + 1))

    def MoveUp(self, contents):
        self.y = max(0, self.y - 1)

    def MoveDown(self, contents):
        self.y = min(len(contents) - 1, self.y + 1)
