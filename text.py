import sys
import msvcrt
import time
import copy
import ctypes

STD_INPUT_HANDLE = -10
STD_OUTPUT_HANDLE= -11
STD_ERROR_HANDLE = -12

FOREGROUND_BLUE = 0x01 # text color contains blue.
FOREGROUND_GREEN= 0x02 # text color contains green.
FOREGROUND_RED  = 0x04 # text color contains red.
FOREGROUND_INTENSITY = 0x08 # text color is intensified.
BACKGROUND_BLUE = 0x10 # background color contains blue.
BACKGROUND_GREEN= 0x20 # background color contains green.
BACKGROUND_RED  = 0x40 # background color contains red.
BACKGROUND_INTENSITY = 0x80 # background color is intensified.

std_out_handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)

attribute_stack = []

class Printable_Structure(ctypes.Structure):
    def __str__(self):
        return str(["({},{},{})".format(str(x),str(y),getattr(self, x)) for x,y in self._fields_])

class COORD(Printable_Structure):
    _fields_ = [
        ("X",ctypes.c_short),
        ("Y",ctypes.c_short)
    ]

WORD = ctypes.c_ushort

class SMALL_RECT(Printable_Structure):
    _fields_ = [
        ("Left", COORD),
        ("Top", COORD),
        ("Right", COORD),
        ("Bottom", COORD)
    ]

class CONSOLE_SCREEN_BUFFER_INFO(Printable_Structure):
    _fields_ = [
        ("dwSize", COORD),
        ("dwCursorPosition", COORD),
        ("wAttributes", WORD),
        ("srWindow", SMALL_RECT),
        ("dwMaximumWindowSize", COORD)
    ]

def set_color(color, handle=std_out_handle):
    bool = ctypes.windll.kernel32.SetConsoleTextAttribute(handle, color)
    return bool

class Cursor:
    def __init__(self):
        self.x = 0
        self.y = 0

def save_console_attributes():
    CURRENT_CONSOLE =  CONSOLE_SCREEN_BUFFER_INFO()
    ctypes.windll.kernel32.GetConsoleScreenBufferInfo(std_out_handle, ctypes.byref(CURRENT_CONSOLE))
    attribute_stack.append(CURRENT_CONSOLE.wAttributes)

def restore_console_attributes():
    bool = ctypes.windll.kernel32.SetConsoleTextAttribute(std_out_handle, attribute_stack.pop())

def draw(contents, cursor):
    drawBuffer = copy.deepcopy(contents)
    if len(drawBuffer[cursor.y]) == 0:
        drawBuffer[cursor.y] = ' '
    for i in range(len(drawBuffer)):
        line = drawBuffer[i]
        for j in range(len(line)):
            c = line[j]
            if i == cursor.y and j == cursor.x:
                save_console_attributes()
                set_color(BACKGROUND_BLUE)
                print(c,end="", flush=True)
                restore_console_attributes()
            else:
                print(c,end="", flush=True)
        print('', flush=True)

def main():
    save_console_attributes()

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
                if b == b'K':
                    cursor.x = max(0, cursor.x - 1)
                elif b == b'M':
                    cursor.x = min(len(contents[cursor.y]) - 1, cursor.x + 1)
                elif b == b'H':
                    cursor.y = max(0, cursor.y - 1)
                    cursor.x = min(len(contents[cursor.y]) - 1, cursor.x)
                elif b == b'P':
                    cursor.y = min(len(contents) - 1, cursor.y + 1)
                    cursor.x = min(len(contents[cursor.y]) - 1, cursor.x)
            print("{},{}".format(a,b))
            print('######################')
            draw(contents, cursor)
        time.sleep(0.01)

    restore_console_attributes()

if __name__=='__main__':
    main()
