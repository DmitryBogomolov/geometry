import unittest
import geometry.relations3 as r3
from geometry.vec3 import Vec3
from geometry.line3 import Line3
from geometry.plane3 import Plane3

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

    def test_point_plane_projection(self):
        plane = Plane3(normal=Vec3(0, 5, 0), distance=4)
        self.assertEqual(r3.point_plane_projection(Vec3(3, 4, 2), plane), Vec3(3, 4, 2))
        self.assertEqual(r3.point_plane_projection(Vec3(0, 4, 9), plane), Vec3(0, 4, 9))
        self.assertEqual(r3.point_plane_projection(Vec3(1, 0, 4), plane), Vec3(1, 4, 4))
        self.assertEqual(r3.point_plane_projection(Vec3(2, 9, 1), plane), Vec3(2, 4, 1))

    def test_point_plane_distance(self):
        plane = Plane3(normal=Vec3(0, 5, 0), distance=4)
        self.assertAlmostEqual(r3.point_plane_distance(Vec3(3, 4, 2), plane), 0)
        self.assertAlmostEqual(r3.point_plane_distance(Vec3(0, 4, 9), plane), 0)
        self.assertAlmostEqual(r3.point_plane_distance(Vec3(1, 0, 4), plane), 4)
        self.assertAlmostEqual(r3.point_plane_distance(Vec3(2, 9, 1), plane), 5)

    def test_line_plane_intersection(self):
        plane = Plane3(normal=Vec3(0, 5, 0), distance=4)
        self.assertEqual(
            r3.line_plane_intersection(
                Line3(anchor=Vec3(4, 2, 0), direction=Vec3(0, 2, 3)),
                plane,
            ),
            Vec3(4, 4, 3),
        )
        self.assertEqual(
            r3.line_plane_intersection(
                Line3(anchor=Vec3(1, 2, 0), direction=Vec3(0, -2, 0)),
                plane,
            ),
            Vec3(1, 4, 0),
        )
        self.assertEqual(
            r3.line_plane_intersection(
                Line3(anchor=Vec3(1, 4, 0), direction=Vec3(2, 0, 2)),
                plane,
            ),
            Line3(anchor=Vec3(1, 4, 0), direction=Vec3(2, 0, 2)),
        )
        self.assertEqual(
            r3.line_plane_intersection(
                Line3(anchor=Vec3(1, 3, 0), direction=Vec3(2, 0, 2)),
                plane,
            ),
            None,
        )

    def test_line_plane_projection(self):
        plane = Plane3(normal=Vec3(0, 5, 0), distance=4)
        self.assertEqual(
            r3.line_plane_projection(
                Line3(anchor=Vec3(1, 3, 2), direction=Vec3(2, 1, 3)),
                plane,
            ),
            Line3(anchor=Vec3(1, 4, 2), direction=Vec3(2, 0, 3)),
        )
        self.assertEqual(
            r3.line_plane_projection(
                Line3(anchor=Vec3(1, 3, 2), direction=Vec3(0, 2, 0)),
                plane,
            ),
            Line3(anchor=Vec3(1, 4, 2), direction=Vec3(0, 2, 0)),
        )

    def test_line_line_distance(self):
        self.assertAlmostEqual(
            r3.line_line_distance(
                Line3(anchor=Vec3(3, 2, 4), direction=Vec3(2, 1, 0)),
                Line3(anchor=Vec3(2, 3, 2), direction=Vec3(1, 2, 0)),
            ),
            2,
        )
        self.assertAlmostEqual(
            r3.line_line_distance(
                Line3(anchor=Vec3(3, 2, 3), direction=Vec3(2, 1, 0)),
                Line3(anchor=Vec3(2, 3, 3), direction=Vec3(1, 2, 0)),
            ),
            0,
        )
        self.assertAlmostEqual(
            r3.line_line_distance(
                Line3(anchor=Vec3(3, 2, 5), direction=Vec3(3, 3, 0)),
                Line3(anchor=Vec3(3, 2, 1), direction=Vec3(3, 3, 0)),
            ),
            4,
        )
        self.assertAlmostEqual(
            r3.line_line_distance(
                Line3(anchor=Vec3(3, 2, 1), direction=Vec3(3, 3, 0)),
                Line3(anchor=Vec3(3, 2, 1), direction=Vec3(3, 3, 0)),
            ),
            0,
        )
