import unittest
import geometry.relations3 as r3
from geometry.vec3 import Vec3
from geometry.line3 import Line3

class TestRelations3(unittest.TestCase):
    def test_point_line_projection(self):
        line = Line3(anchor=Vec3(0, 3, 0), direction=Vec3(2, 0, 2))
        self.assertEqual(r3.point_line_projection(Vec3(1, 3, 1), line), Vec3(1, 3, 1))
        self.assertEqual(r3.point_line_projection(Vec3(4, 3, 4), line), Vec3(4, 3, 4))
        self.assertEqual(r3.point_line_projection(Vec3(2, 0, 2), line), Vec3(2, 3, 2))
        self.assertEqual(r3.point_line_projection(Vec3(4, 3, 0), line), Vec3(2, 3, 2))

    def test_point_line_distance(self):
        line = Line3(anchor=Vec3(0, 3, 0), direction=Vec3(2, 0, 2))
        self.assertAlmostEqual(r3.point_line_distance(Vec3(1, 3, 1), line), 0)
        self.assertAlmostEqual(r3.point_line_distance(Vec3(4, 3, 4), line), 0)
        self.assertAlmostEqual(r3.point_line_distance(Vec3(2, 0, 2), line), 3)
        self.assertAlmostEqual(r3.point_line_distance(Vec3(4, 3, 0), line), 2.82842712)
