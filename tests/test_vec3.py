import unittest

from geometry.vec3 import Vec3

class TestVec3(unittest.TestCase):
    def test_vec3(self):
        v = Vec3(1, 2, 3)
        self.assertEqual(v.x, 1)
        self.assertEqual(v.y, 2)
        self.assertEqual(v.z, 3)
