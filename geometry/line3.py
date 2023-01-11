from typing import NamedTuple
from .vec3 import Vec3, ZERO3, XUNIT3, YUNIT3, ZUNIT3, eq3

class Line3(NamedTuple):
    anchor: Vec3
    direction: Vec3

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Line3):
            return eq_line3(self, other)
        return False

OX3 = Line3(anchor=ZERO3, direction=XUNIT3)
OY3 = Line3(anchor=ZERO3, direction=YUNIT3)
OZ3 = Line3(anchor=ZERO3, direction=ZUNIT3)

def eq_line3(a: Line3, b: Line3) -> bool:
    return eq3(a.anchor, b.anchor) and eq3(a.direction, b.direction)
