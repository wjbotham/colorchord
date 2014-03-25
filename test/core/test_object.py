import unittest
from core.object import Object

class TestObject(unittest.TestCase):
    def test_distance(self):
        a = Object(10,5)
        self.assertEqual(a.distance(a), 0)
        b = Object(0,0)
        self.assertEqual(a.distance(b), 125**0.5)
        self.assertEqual(b.distance(a), 125**0.5)
        c = Object(5.25,5)
        self.assertEqual(a.distance(c), 4.75)

    def test_motion(self):
        a = Object(0,0,5.5,4)
        a.tick()
        self.assertEqual(a.x, 5.5)
        self.assertEqual(a.y, 4)
        a.tick()
        self.assertEqual(a.x, 11)
        self.assertEqual(a.y, 8)
        a.dx = -1
        a.dy = -0.5
        a.tick()
        self.assertEqual(a.x, 10)
        self.assertEqual(a.y, 7.5)

    def test_lifespan(self):
        a = Object(0,0,0,0,2)
        self.assertTrue(not a.needs_cleanup)
        a.tick()
        self.assertTrue(not a.needs_cleanup)
        a.tick()
        self.assertTrue(a.needs_cleanup)

    def test_position(self):
        a = Object(0.4,0.6)
        self.assertEqual(a.position, (0,1))
        b = Object(1,2)
        self.assertEqual(b.position, (1,2))
        c = Object(31.1,1/3)
        self.assertEqual(c.position, (31,0))
