import unittest
# pylint: disable=W0401,W0614
from geometry.vec3 import *

class TestVec3(unittest.TestCase):
    def test_constants(self):
        self.assertEqual(ZERO3, Vec3(0, 0, 0))
        self.assertEqual(UNIT3, Vec3(1, 1, 1))
        self.assertEqual(XUNIT3, Vec3(1, 0, 0))
        self.assertEqual(YUNIT3, Vec3(0, 1, 0))
        self.assertEqual(ZUNIT3, Vec3(0, 0, 1))

    def test_eq3(self):
        self.assertEqual(eq3(Vec3(1, 2, 3), Vec3(1, 2, 3)), True)
        self.assertEqual(eq3(Vec3(1, 2, 3), Vec3(2, 3, 1)), False)

    def test_dot3(self):
        self.assertEqual(dot3(Vec3(1, 2, 3), Vec3(2, 3, 4)), 20)
        self.assertEqual(dot3(Vec3(1, 2, 0), Vec3(0, 0, 3)), 0)

    def test_len3(self):
        self.assertAlmostEqual(len3(Vec3(1, 2, 3)), 3.74165739)

    def test_is_zero3(self):
        self.assertEqual(is_zero3(Vec3(1, 2, 3)), False)
        self.assertEqual(is_zero3(Vec3(0, 0, 0)), True)

    def test_is_unit3(self):
        self.assertEqual(is_unit3(Vec3(1, 0, 0)), True)
        self.assertEqual(is_unit3(Vec3(0, 1, 0)), True)
        self.assertEqual(is_unit3(Vec3(0, 0, 1)), True)
        self.assertEqual(is_unit3(Vec3(1, 1, 1)), False)
        self.assertEqual(is_unit3(Vec3(1 / 3, 2 / 3, 2 / 3)), True)

    def test_mul3(self):
        self.assertEqual(mul3(Vec3(1, 2, 3), 2), Vec3(2, 4, 6))

    def test_pos3(self):
        self.assertEqual(pos3(Vec3(1, 2, 3)), Vec3(1, 2, 3))

    def test_neg3(self):
        self.assertEqual(neg3(Vec3(1, 2, 3)), Vec3(-1, -2, -3))

    def test_norm3(self):
        self.assertEqual(norm3(Vec3(0, 0, 0)), Vec3(0, 0, 0))
        self.assertEqual(norm3(Vec3(1, 2, 2)), Vec3(1 / 3, 2 / 3, 2 / 3))

    def test_add3(self):
        self.assertEqual(add3(Vec3(1, 2, 3), Vec3(2, 3, 4)), Vec3(3, 5, 7))

    def test_sub3(self):
        self.assertEqual(sub3(Vec3(1, 2, 3), Vec3(2, 3, 4)), Vec3(-1, -1, -1))

    def test_cross3(self):
        self.assertEqual(cross3(Vec3(1, 2, 3), Vec3(2, 3, 4)), Vec3(-1, 2, -1))

    def test_angle3(self):
        self.assertAlmostEqual(angle3(Vec3(1, 2, 3), Vec3(2, 3, 4)), 0.12186757)

    def test_orthogonal3(self):
        self.assertEqual(orthogonal3(Vec3(1, 2, 3), Vec3(1, 2, 3)), False)
        self.assertEqual(orthogonal3(Vec3(1, 2, 3), Vec3(0, 0, 0)), True)
        self.assertEqual(orthogonal3(Vec3(1, 2, 3), Vec3(-1, -1, 1)), True)

    def test_collinear3(self):
        self.assertEqual(collinear3(Vec3(1, 2, 3), Vec3(1, 2, 3)), True)
        self.assertEqual(collinear3(Vec3(1, 2, 3), Vec3(-1, -2, -3)), True)
        self.assertEqual(collinear3(Vec3(1, 2, 3), Vec3(1, -2, 3)), False)

    def test_rotate3(self):
        self.assertEqual(rotate3(Vec3(1, 2, 3), Vec3(2, 0, 0), math.pi / 2), Vec3(1, -3, 2))
        self.assertEqual(rotate3(Vec3(1, 2, 3), Vec3(0, 3, 0), math.pi / 2), Vec3(3, 2, -1))
        self.assertEqual(rotate3(Vec3(1, 2, 3), Vec3(0, 0, 4), math.pi / 2), Vec3(-2, -1, 3))

    def test_project3(self):
        self.assertEqual(project3(Vec3(1, 2, 3), Vec3(2, 0, 0)), Vec3(1, 0, 0))
        self.assertEqual(project3(Vec3(1, 2, 3), Vec3(0, 3, 0)), Vec3(0, 2, 0))
        self.assertEqual(project3(Vec3(1, 2, 3), Vec3(0, 0, 4)), Vec3(0, 0, 3))
        self.assertEqual(project3(Vec3(1, 2, 3), Vec3(-2, -4, 0)), Vec3(1, 2, 0))
        self.assertEqual(project3(Vec3(1, 2, 3), Vec3(-2, -4, -6)), Vec3(1, 2, 3))
