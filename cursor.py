class Cursor:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "({},{})".format(self.x, self.y)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.x == other.x and self.y == other.y
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, self.__class__):
            return not self == other
        return NotImplemented

    def __hash__(self):
        return hash((self.x,self.y))

    def MoveLeft(self, contents):
        self.x = max(0, min(self.x - 1, len(contents[self.y]) - 1))

    def MoveRight(self, contents):
        self.x = max(0, min(len(contents[self.y]) - 1, self.x + 1))

    def MoveUp(self, contents):
        self.y = max(0, self.y - 1)

    def MoveDown(self, contents):
        self.y = min(len(contents) - 1, self.y + 1)
