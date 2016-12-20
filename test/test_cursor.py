import unittest

from cursor import Cursor

class TestCursorMovement(unittest.TestCase):
    def test_MoveLeftEmptyContent_0(self):
        c = Cursor()
        contents = [[]]
        c.MoveLeft(contents)
        self.assertEqual(c.x,0)
        self.assertEqual(c.y,0)

    def test_MoveRightEmptyContent_0(self):
        c = Cursor()
        contents = [[]]
        c.MoveRight(contents)
        self.assertEqual(c.x,0)
        self.assertEqual(c.y,0)

    def test_MoveUpEmptyContent_0(self):
        c = Cursor()
        contents = [[]]
        c.MoveUp(contents)
        self.assertEqual(c.x,0)
        self.assertEqual(c.y,0)

    def test_MoveDownEmptyContent_0(self):
        c = Cursor()
        contents = [[]]
        c.MoveDown(contents)
        self.assertEqual(c.x,0)
        self.assertEqual(c.y,0)


if __name__ == '__main__':
    unittest.main()
