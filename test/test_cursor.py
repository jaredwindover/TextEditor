import unittest

from cursor import Cursor

class TestCursorMovement(unittest.TestCase):
    def test_MovementEmptyContent(self):
        contents = [[]]
        expectedCursor = Cursor(0,0)
        cursor = Cursor(0,0)
        for cursorFunc in [
                cursor.MoveLeft,
                cursor.MoveRight,
                cursor.MoveUp,
                cursor.MoveDown
        ]:
            cursorFunc(contents)
            self.assertEqual(cursor,expectedCursor)

    def test_MoveRightEmptyContent_0_0(self):
        c = Cursor()
        contents = [[]]
        c.MoveRight(contents)
        self.assertEqual(c.x,0)
        self.assertEqual(c.y,0)

    def test_MoveUpEmptyContent_0_0(self):
        c = Cursor()
        contents = [[]]
        c.MoveUp(contents)
        self.assertEqual(c.x,0)
        self.assertEqual(c.y,0)

    def test_MoveDownEmptyContent_0_0(self):
        c = Cursor()
        contents = [[]]
        c.MoveDown(contents)
        self.assertEqual(c.x,0)
        self.assertEqual(c.y,0)

    def test_MoveLeftOneChar_0_0(self):
        c = Cursor()
        contents = [['a']]
        c.MoveLeft(contents)
        self.assertEqual(c.x,0)
        self.assertEqual(c.y,0)


if __name__ == '__main__':
    unittest.main()
