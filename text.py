import sys
import msvcrt
import time
import copy
import console
from cursor import Cursor

class Keys:
    LeftArrow = b'K'
    RightArrow = b'M'
    UpArrow = b'H'
    DownArrow = b'P'

def draw(contents, cursor):
    cursorBuffer = copy.deepcopy(cursor)
    drawBuffer = copy.deepcopy(contents)
    if len(drawBuffer[cursorBuffer.y]) < cursorBuffer.x:
        cursorBuffer.x = len(drawBuffer[cursorBuffer.y])
    for i in range(len(drawBuffer)):
        line = drawBuffer[i] + [' ']
        for j in range(len(line)):
            c = line[j]
            if i == cursorBuffer.y and j == cursorBuffer.x:
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
            print("Last Key: {},{}".format(a,b))
            print("Cursor: {}".format(cursor))
            print('_________________________')
            draw(contents, cursor)
        time.sleep(0.01)

if __name__=='__main__':
    main()
