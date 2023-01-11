import unittest
# pylint: disable=W0401,W0614
from geometry.line3 import *

class TestLine3(unittest.TestCase):
    def test_constants(self):
        self.assertEqual(OX3, Line3(anchor=Vec3(0, 0, 0), direction=Vec3(1, 0, 0)))
        self.assertEqual(OY3, Line3(anchor=Vec3(0, 0, 0), direction=Vec3(0, 1, 0)))
        self.assertEqual(OZ3, Line3(anchor=Vec3(0, 0, 0), direction=Vec3(0, 0, 1)))

    def test_eq_line3(self):
        self.assertEqual(eq_line3(
            Line3(anchor=Vec3(1, 2, 3), direction=Vec3(2, 3, 4)),
            Line3(anchor=Vec3(1, 2, 3), direction=Vec3(2, 3, 4))
        ), True)
        self.assertEqual(eq_line3(
            Line3(anchor=Vec3(1, 2, 3), direction=Vec3(2, 3, 4)),
            Line3(anchor=Vec3(2, 3, 1), direction=Vec3(2, 3, 4))
        ), False)
