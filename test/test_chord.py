import unittest
from color.chord import Chord
from color.note import Note

class TestChord(unittest.TestCase):
    def setUp(self):
        self.null               = Chord()
        self.pure               = Chord(Note(5))
        self.pureStrong         = Chord(Note(5)*2)
        self.overlap            = Chord(Note(1), Note(1))
        self.three              = Chord(Note(1), Note(2),   Note(3))
        self.threeReversed      = Chord(Note(3), Note(2),   Note(1))
        self.purePlusThree      = Chord(Note(5), Note(1),   Note(2),   Note(3))
        self.threeHigh          = Chord(Note(2), Note(3),   Note(4))
        self.threePlusThreeHigh = Chord(Note(1), Note(2)*2, Note(3)*2, Note(4)*2)

    def test_init(self):
        self.assertEqual(len(self.null.notes), 0)
        self.assertEqual(len(self.pure.notes), 1)
        self.assertEqual(len(self.three.notes), 3)
        self.assertEqual(len(self.overlap.notes), 1)
        self.assertEqual(self.overlap.notes[0].intensity, 2)

    def test_add(self):
        self.assertEqual(self.null + self.pure, self.pure)
        self.assertEqual(self.null + self.three, self.three)
        self.assertEqual(self.pure + self.three, self.purePlusThree)

    def test_mult(self):
        self.assertEqual(self.null * 4, self.null)
        self.assertEqual(self.pure * 2, self.pureStrong)
