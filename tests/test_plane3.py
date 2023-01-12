import unittest
# pylint: disable=W0401,W0614
from geometry.plane3 import *

class TestPlane3(unittest.TestCase):
    def test_constants(self):
        self.assertEqual(XOY3, Plane3(normal=Vec3(0, 0, 1), distance=0))
        self.assertEqual(YOZ3, Plane3(normal=Vec3(1, 0, 0), distance=0))
        self.assertEqual(ZOX3, Plane3(normal=Vec3(0, 1, 0), distance=0))

    def test_eq_plane3(self):
        self.assertEqual(eq_plane3(
            Plane3(normal=Vec3(1, 2, 3), distance=4),
            Plane3(normal=Vec3(1, 2, 3), distance=4)
        ), True)
        self.assertEqual(eq_plane3(
            Plane3(normal=Vec3(1, 2, 3), distance=4),
            Plane3(normal=Vec3(2, 3, 1), distance=4)
        ), False)
