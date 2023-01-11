from typing import NamedTuple
import math

class Vec3(NamedTuple):
    x: float
    y: float
    z: float

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Vec3):
            return eq3(self, other)
        return False

def _eq(a: float, b: float) -> bool:
    return abs(a - b) < 1E-8

ZERO3 = Vec3(0, 0, 0)
UNIT3 = Vec3(1, 1, 1)
XUNIT3 = Vec3(1, 0, 0)
YUNIT3 = Vec3(0, 1, 0)
ZUNIT3 = Vec3(0, 0, 1)

def eq3(a: Vec3, b: Vec3) -> bool:
    return _eq(a.x, b.x) and _eq(a.y, b.y) and _eq(a.z, b.z)

def dot3(a: Vec3, b: Vec3) -> float:
    return a.x * b.x + a.y * b.y + a.z * b.z

def len3(v: Vec3) -> float:
    return math.sqrt(dot3(v, v))

def is_zero3(v: Vec3) -> bool:
    return _eq(dot3(v, v), 0)

def is_unit3(v: Vec3) -> bool:
    return _eq(dot3(v, v), 1)

def mul3(v: Vec3, k: float) -> Vec3:
    return Vec3(v.x * k, v.y * k, v.z * k)

def neg3(v: Vec3) -> Vec3:
    return mul3(v, -1)

def pos3(v: Vec3) -> Vec3:
    return mul3(v, +1)

def norm3(v: Vec3) -> Vec3:
    vec_len = len3(v)
    return mul3(v, 1 / vec_len) if not _eq(vec_len, 0) else ZERO3

def add3(a: Vec3, b: Vec3) -> Vec3:
    return Vec3(a.x + b.x, a.y + b.y, a.z + b.z)

def sub3(a: Vec3, b: Vec3) -> Vec3:
    return Vec3(a.x - b.x, a.y - b.y, a.z - b.z)

def cross3(a: Vec3, b: Vec3) -> Vec3:
    return Vec3(a.y * b.z - a.z * b.y, a.z * b.x - a.x * b.z, a.x * b.y - a.y * b.x)

def angle3(a: Vec3, b: Vec3) -> float:
    return math.acos(dot3(norm3(a), norm3(b)))

def orthogonal3(a: Vec3, b: Vec3) -> bool:
    return _eq(dot3(a, b), 0)

def collinear3(a: Vec3, b: Vec3) -> bool:
    return is_zero3(cross3(a, b))

def rotate3(v: Vec3, axis: Vec3, angle: float) -> Vec3:
    c = math.cos(angle)
    s = math.sin(angle)
    t = 1 - c
    (x, y, z) = norm3(axis)
    return Vec3(
        v.x * (x * x * t + c) + v.y * (x * y * t - z * s) + v.z * (x * z * t + y * s),
        v.x * (y * x * t - z * s) + v.y * (y * y * t + c) + v.z * (y * z * t - x * s),
        v.x * (z * x * t - y * s) + v.y * (z * y * t + x * s) + v.z * (z * z * t + c),
    )

def project3(v: Vec3, axis: Vec3) -> Vec3:
    vec_dir = norm3(axis)
    vec_len = dot3(v, vec_dir)
    return mul3(vec_dir, vec_len)
