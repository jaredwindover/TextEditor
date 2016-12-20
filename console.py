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

class state:
    attribute_stack = []

    def __init__(self, new_attribute):
        self.attribute = new_attribute

    def __enter__(self):
        CURRENT_CONSOLE =  CONSOLE_SCREEN_BUFFER_INFO()
        ctypes.windll.kernel32.GetConsoleScreenBufferInfo(
            std_out_handle,
            ctypes.byref(CURRENT_CONSOLE))
        state.attribute_stack.append(CURRENT_CONSOLE.wAttributes)
        ctypes.windll.kernel32.SetConsoleTextAttribute(std_out_handle, self.attribute)

    def __exit__(self, type, value, traceback):
        ctypes.windll.kernel32.SetConsoleTextAttribute(
            std_out_handle,
            state.attribute_stack.pop())
