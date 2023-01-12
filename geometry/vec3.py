import typing
import math

class Vec3(typing.NamedTuple):
    x: float
    y: float
    z: float

    def __eq__(self, other: object) -> bool:
        try:
            return eq3(self, typing.cast(Vec3, other))
        except: # pylint: disable=bare-except
            return False

ZERO3 = Vec3(0, 0, 0)
UNIT3 = Vec3(1, 1, 1)
XUNIT3 = Vec3(1, 0, 0)
YUNIT3 = Vec3(0, 1, 0)
ZUNIT3 = Vec3(0, 0, 1)

def eq3(a: Vec3, b: Vec3) -> bool:
    (ax, ay, az) = a
    (bx, by, bz) = b
    return math.isclose(ax, bx) and math.isclose(ay, by) and math.isclose(az, bz)

def dot3(a: Vec3, b: Vec3) -> float:
    (ax, ay, az) = a
    (bx, by, bz) = b
    return ax * bx + ay * by + az * bz

def len3(v: Vec3) -> float:
    return math.sqrt(dot3(v, v))

def is_zero3(v: Vec3) -> bool:
    return math.isclose(dot3(v, v), 0)

def is_unit3(v: Vec3) -> bool:
    return math.isclose(dot3(v, v), 1)

def mul3(v: Vec3, k: float) -> Vec3:
    (vx, vy, vz) = v
    return Vec3(vx * k, vy * k, vz * k)

def neg3(v: Vec3) -> Vec3:
    return mul3(v, -1)

def pos3(v: Vec3) -> Vec3:
    return mul3(v, +1)

def norm3(v: Vec3) -> Vec3:
    vec_len = len3(v)
    return mul3(v, 1 / vec_len) if not math.isclose(vec_len, 0) else ZERO3

def add3(a: Vec3, b: Vec3) -> Vec3:
    (ax, ay, az) = a
    (bx, by, bz) = b
    return Vec3(ax + bx, ay + by, az + bz)

def sub3(a: Vec3, b: Vec3) -> Vec3:
    (ax, ay, az) = a
    (bx, by, bz) = b
    return Vec3(ax - bx, ay - by, az - bz)

def cross3(a: Vec3, b: Vec3) -> Vec3:
    (ax, ay, az) = a
    (bx, by, bz) = b
    return Vec3(ay * bz - az * by, az * bx - ax * bz, ax * by - ay * bx)

def angle3(a: Vec3, b: Vec3) -> float:
    return math.acos(dot3(norm3(a), norm3(b)))

def orthogonal3(a: Vec3, b: Vec3) -> bool:
    return math.isclose(dot3(a, b), 0)

def collinear3(a: Vec3, b: Vec3) -> bool:
    return is_zero3(cross3(a, b))

def rotate3(v: Vec3, axis: Vec3, angle: float) -> Vec3:
    c = math.cos(angle)
    s = math.sin(angle)
    t = 1 - c
    (nx, ny, nz) = norm3(axis)
    (vx, vy, vz) = v
    return Vec3(
        vx * (nx * nx * t + c) + vy * (nx * ny * t - nz * s) + vz * (nx * nz * t + ny * s),
        vx * (ny * nx * t - nz * s) + vy * (ny * ny * t + c) + vz * (ny * nz * t - nx * s),
        vx * (nz * nx * t - ny * s) + vy * (nz * ny * t + nx * s) + vz * (nz * nz * t + c),
    )

def project3(v: Vec3, axis: Vec3) -> Vec3:
    vec_dir = norm3(axis)
    vec_len = dot3(v, vec_dir)
    return mul3(vec_dir, vec_len)
