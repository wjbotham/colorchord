import unittest
from color.note import Note

class TestNote(unittest.TestCase):
    def test_add(self):
        weak = Note(1.8)
        strong = Note(1.8)*2
        weakPlusStrong = weak+strong
        self.assertEqual(len(weakPlusStrong.notes), 1)
        self.assertEqual(weakPlusStrong.notes[0].frequency, 1.8)
        self.assertEqual(weakPlusStrong.notes[0].intensity, 3)

    def test_mult(self):
        a = Note(1.8)
        a_six = a*6
        self.assertEqual(a_six.intensity, 6)
