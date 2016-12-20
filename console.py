import ctypes
from additional_wintypes import CONSOLE_SCREEN_BUFFER_INFO

class state:
    attribute_stack = []

    def __init__(self, handle, new_attribute):
        self.handle = handle
        self.attribute = new_attribute

    def __enter__(self):
        current_console =  CONSOLE_SCREEN_BUFFER_INFO()
        ctypes.windll.kernel32.GetConsoleScreenBufferInfo(
            self.handle,
            ctypes.byref(current_console))
        state.attribute_stack.append(current_console.wAttributes)
        ctypes.windll.kernel32.SetConsoleTextAttribute(self.handle, self.attribute)

    def __exit__(self, type, value, traceback):
        ctypes.windll.kernel32.SetConsoleTextAttribute(
            self.handle,
            state.attribute_stack.pop())
