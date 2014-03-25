import unittest
from color.chord import Note

class TestChord(unittest.TestCase):
    def test_add(self):
        a = Note(5) + 0
        b = Note(5)
        self.assertEqual(a, b)
        self.assertEqual(a.notes[5], 1)
        a = Note(1) + Note(2)
        b = Note(2) + Note(1)
        self.assertEqual(a, b)
        self.assertEqual(a.notes[1], 1)
        self.assertEqual(a.notes[2], 1)
        a =  Note(1) + (Note(2) + Note(3))
        b = (Note(1) +  Note(2)) + Note(3)
        self.assertEqual(a, b)
        self.assertEqual(a.notes[1], 1)
        self.assertEqual(a.notes[2], 1)
        self.assertEqual(a.notes[3], 1)
        a = Note(6) + Note(6) + Note(6)
        self.assertEqual(a.notes[6], 3)

    def test_mult(self):
        a = Note(1) * 2
        self.assertEqual(a.notes[1], 2)
        a = 3 * Note(2)
        self.assertEqual(a.notes[2], 3)

    def test_div(self):
        a = Note(1) / 2
        self.assertEqual(a.notes[1], 1/2)

    def test_repr(self):
        a = Note(5)
        self.assertEqual(eval(repr(a)), a)
        a = Note(1) + Note(2)
        self.assertEqual(eval(repr(a)), a)
        a = Note(1)*2 + Note(5)
        self.assertEqual(eval(repr(a)), a)
