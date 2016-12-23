import unittest
from gentests import gentests, vals
from cursor import Cursor

@gentests
class TestCursorMovement(unittest.TestCase):

    @vals([
        Cursor.MoveLeft,
        Cursor.MoveRight,
        Cursor.MoveUp,
        Cursor.MoveDown
    ])
    def test_MovementEmptyContent(self, cursorFunc):
        contents = [[]]
        expectedCursor = Cursor(0,0)
        cursor = Cursor(0,0)
        cursorFunc(cursor, contents)
        self.assertEqual(cursor,expectedCursor)

    def name_test(original_name, cursorFunc, expectedCursor):
        return '{0}_Cursor_{1}_{2}_{3}'.format(
            original_name,
            cursorFunc.__name__,
            str(expectedCursor.x),
            str(expectedCursor.y)
        )

    @vals([
        (Cursor.MoveLeft, Cursor(0,0)),
        (Cursor.MoveRight, Cursor(1,0)),
        (Cursor.MoveUp, Cursor(0,0)),
        (Cursor.MoveDown, Cursor(0,0))
    ], name=name_test)
    def test_MovementOneChar_StartLeft(self, cursorFunc, expectedCursor):
        contents = [['a']]
        cursor = Cursor(0,0)
        cursorFunc(cursor, contents)
        self.assertEqual(cursor,expectedCursor)

    @vals([
        (Cursor.MoveLeft, Cursor(0,0)),
        (Cursor.MoveRight, Cursor(1,0)),
        (Cursor.MoveUp, Cursor(0,0)),
        (Cursor.MoveDown, Cursor(0,0))
    ], name=name_test)
    def test_MovementOneChar_StartRight(self, cursorFunc, expectedCursor):
        contents = [['a']]
        cursor = Cursor(1,0)
        cursorFunc(cursor, contents)
        self.assertEqual(cursor,expectedCursor)

if __name__ == '__main__':
    unittest.main()
