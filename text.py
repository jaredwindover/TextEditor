import sys
import msvcrt
import time
import copy
import console

class Keys:
    LeftArrow = b'K'
    RightArrow = b'M'
    UpArrow = b'H'
    DownArrow = b'P'

class Cursor:
    def __init__(self):
        self.x = 0
        self.y = 0

    def __str__(self):
        return "({},{})".format(self.x, self.y)

    def MoveLeft(self, contents):
        self.x = max(0, self.x - 1)

    def MoveRight(self, contents):
        self.x = min(len(contents[self.y]) - 1, self.x + 1)

    def MoveUp(self, contents):
        self.y = max(0, self.y - 1)
        self.x = max(0, min(len(contents[self.y]) - 1, self.x))

    def MoveDown(self, contents):
        self.y = min(len(contents) - 1, self.y + 1)
        self.x = max(0, min(len(contents[self.y]) - 1, self.x))

def draw(contents, cursor):
    drawBuffer = copy.deepcopy(contents)
    if len(drawBuffer[cursor.y]) == 0:
        drawBuffer[cursor.y] = ' '
    for i in range(len(drawBuffer)):
        line = drawBuffer[i]
        for j in range(len(line)):
            c = line[j]
            if i == cursor.y and j == cursor.x:
                with console.state(console.BACKGROUND_BLUE):
                    print(c,end="", flush=True)
            else:
                print(c,end="", flush=True)
        print('', flush=True)

def main():
    file = sys.argv[1]
    contents = [[y for y in x] for x in open(file).read().split('\n')]
    cursor = Cursor()

    done = False
    draw(contents, cursor)
    while not done:
        if msvcrt.kbhit():
            a = msvcrt.getch()
            b = b'\x00'
            if a == b'\x00' or a == b'\xe0':
                b = msvcrt.getch()
            if a == b'\x11':
                done = True
            if a == b'\xe0':
                {
                    Keys.LeftArrow : cursor.MoveLeft,
                    Keys.RightArrow : cursor.MoveRight,
                    Keys.UpArrow : cursor.MoveUp,
                    Keys.DownArrow : cursor.MoveDown
                }[b](contents)
                #if b == b'K':
                #    cursor.MoveLeft(contents)
                #elif b == b'M':
                #    cursor.MoveRight(contents)
                #elif b == b'H':
                #    cursor.MoveUp(contents)
                #elif b == b'P':
                #    cursor.MoveDown(contents)
            print("Last Key: {},{}".format(a,b))
            print("Cursor: {}".format(cursor))
            print('_________________________')
            draw(contents, cursor)
        time.sleep(0.01)

if __name__=='__main__':
    main()
