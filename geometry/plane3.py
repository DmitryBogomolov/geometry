import typing
import math
from .vec3 import Vec3, XUNIT3, YUNIT3, ZUNIT3, eq3

class Plane3(typing.NamedTuple):
    normal: Vec3
    distance: float

    def __eq__(self, other: object) -> bool:
        try:
            return eq_plane3(self, typing.cast(Plane3, other))
        except: # pylint: disable=bare-except
            return False

XOY3 = Plane3(normal=ZUNIT3, distance=0)
YOZ3 = Plane3(normal=XUNIT3, distance=0)
ZOX3 = Plane3(normal=YUNIT3, distance=0)

def eq_plane3(a: Plane3, b: Plane3) -> bool:
    return eq3(a.normal, b.normal) and math.isclose(a.distance, b.distance)
