import typing
import math
from .vec3 import Vec3, add3, sub3, mul3, len3, project3, norm3, dot3, is_zero3, cross3
from .line3 import Line3
from .plane3 import Plane3

def point_line_projection(target_point: Vec3, line: Line3) -> Vec3:
    '''Projects point onto line.

    For an arbitrary line point project vector from line point to target point onto line.
    Offset line point by that projection.
    '''
    line_point_to_target_dir = sub3(target_point, line.anchor)
    line_point_to_target_proj = project3(line_point_to_target_dir, line.direction)
    return add3(line.anchor, line_point_to_target_proj)

def point_line_distance(target_point: Vec3, line: Line3) -> float:
    '''Finds distance from point to line.

    Take distance between target point and its projection onto line.
    '''
    target_point_proj = point_line_projection(target_point, line)
    return len3(sub3(target_point, target_point_proj))

def point_plane_projection(target_point: Vec3, plane: Plane3) -> Vec3:
    '''Projects point onto plane.

    For an arbitrary plane point project vector from target point to plane point onto plane normal.
    Offset target point by that projection.

    Set of plane points is defined by the equation: `(normalized_normal, x) = distance`.
    '''
    plane_point = mul3(norm3(plane.normal), plane.distance)
    target_to_plane_point_dir = sub3(plane_point, target_point)
    target_to_plane_point_proj = project3(target_to_plane_point_dir, plane.normal)
    return add3(target_point, target_to_plane_point_proj)

def point_plane_distance(target_point: Vec3, plane: Plane3) -> float:
    '''Finds distance from point to plane.

    Take distance between target point and its projection onto plane.
    '''
    target_point_proj = point_plane_projection(target_point, plane)
    return len3(sub3(target_point, target_point_proj))

def line_plane_intersection(line: Line3, plane: Plane3) -> typing.Union[Vec3, Line3, None]:
    '''Finds intersection of line and plane.

    Set of line points is defined by the equation: `anchor + direction * t = x`
    Set of plane points is defined by the equation: `(normalized_normal, x) = distance`

    Substitution of x gives
    `(normalized_normal, anchor) + (normalized_normal, direction) * t = distance`
    `t = (distance - (normalized_normal, anchor)) / (normalized_normal, direction)`

    If line direction is orthogonal to plane normal then either no intersection or
    line belongs to plane (if line point belongs to plane).
    Otherwise t defines one intersection point.
    '''
    plane_normal = norm3(plane.normal)
    num = plane.distance - dot3(line.anchor, plane_normal)
    den = dot3(line.direction, plane_normal)
    if math.isclose(num, 0) and math.isclose(den, 0):
        return line
    if math.isclose(den, 0):
        return None
    return add3(line.anchor, mul3(line.direction, num / den))

def line_plane_projection(line: Line3, plane: Plane3) -> Line3:
    '''Projects line onto plane.

    Take two line points, project them onto plane.
    If line is orthogonal to plane then two projected points are same.
    In that case use original line direction.
    '''

    anchor_proj = point_plane_projection(line.anchor, plane)
    other_anchor = add3(line.anchor, line.direction)
    other_anchor_proj = point_plane_projection(other_anchor, plane)
    direction_proj = sub3(other_anchor_proj, anchor_proj)
    if is_zero3(direction_proj):
        return Line3(anchor=anchor_proj, direction=line.direction)
    return Line3(anchor=anchor_proj, direction=direction_proj)

def line_line_distance(a_line: Line3, b_line: Line3) -> float:
    '''Finds distance between two lines.

    Cross product of lines directions gives normal that defines set of planes.
    Plane that contains line 1: `(normal, line_1_point) = distance_1`.
    Plane that contains line 2: `(normal, line_2_point) = distance_2`.
    Distance between planes: `(normal, line_1_point - line_2_point)`.

    If lines are collinear then take distance from point of one line to other line.
    '''
    normal = norm3(cross3(a_line.direction, b_line.direction))
    if is_zero3(normal):
        return point_line_distance(a_line.anchor, b_line)
    return abs(dot3(normal, sub3(a_line.anchor, b_line.anchor)))

def line_line_intersection(a_line: Line3, b_line: Line3) -> \
    typing.Union[typing.Tuple[Vec3, Vec3], None]:
    '''Finds intersection between two lines.

    Line 1: `p1 = r1 + t1 * e1`.
    Line 2: `p2 = r2 + t2 * e2`.
    Cross product of lines directions gives normal that defines set of planes: `n = e1 x e2`.
    Cross product of lines directions and plane normal gives lines normals.
    Intersection point, line 1 point, line 2 point form triangle on that plane.

    For line 1 projection of `r2 - r1` onto line 2 normal gives side of right-angled triangle.
    Angle sine is given by cross product: `|n| = |e1| * |e2| * sin`.
    Hypotenuse of triangle gives distance from `r1` to intersection point.
    Semiplanes (`e2`) of `r2 - r1` and `e1` give distance direction.
    `|n| / (|e1| * |e2|) * |(e2 x n, r2 - r1)| / |e2 x n|
        * sign(e2 x n, r2 - r1) * sign(e2 x n, e1)`
    After simplification
    `(|e1| / (n, n)) * (e2 x n, r2 - r1) * sign(e2 x n, e1)`
    So
    `t1 = (1 / (n, n)) * (e2 x n, r2 - r1) * sign(e2 x n, e1)`
    `t2 = (1 / (n, n)) * (e1 x n, r1 - r2) * sign(e1 x n, e2)`
    Similarly for line 2.

    If lines are collinear then no intersection.
    '''
    normal = cross3(a_line.direction, b_line.direction)
    if is_zero3(normal):
        return None
    a_normal = cross3(a_line.direction, normal)
    b_normal = cross3(b_line.direction, normal)
    k = 1 / dot3(normal, normal)
    a_t = k * dot3(b_normal, sub3(b_line.anchor, a_line.anchor)) \
        * math.copysign(1, dot3(b_normal, a_line.direction))
    b_t = k * dot3(a_normal, sub3(a_line.anchor, b_line.anchor)) \
        * math.copysign(1, dot3(a_normal, b_line.direction))
    return (
        add3(a_line.anchor, mul3(a_line.direction, a_t)),
        add3(b_line.anchor, mul3(b_line.direction, b_t)),
    )

def plane_plane_intersection(a_plane: Plane3, b_plane: Plane3) -> typing.Union[Line3, None]:
    '''Finds intersection between planes.

    Cross product of planes normals gives line direction.
    Pick point on each line (for certainty pick closest to (0,0,0) points).
    Cross products of planes normals and line direction gives directions of intersecting lines.
    Find intersection point. Take it as intersection line point.

    If planes are parallel then no intersection.
    '''

    direction = cross3(a_plane.normal, b_plane.normal)
    if is_zero3(direction):
        return None
    a_anchor = mul3(norm3(a_plane.normal), a_plane.distance)
    b_anchor = mul3(norm3(b_plane.normal), b_plane.distance)
    a_direction = cross3(a_plane.normal, direction)
    b_direction = cross3(b_plane.normal, direction)
    a_point, b_point = typing.cast(typing.Tuple[Vec3, Vec3], line_line_intersection(
        Line3(anchor=a_anchor, direction=a_direction),
        Line3(anchor=b_anchor, direction=b_direction)
    ))
    # They are equal actually.
    point = mul3(add3(a_point, b_point), 0.5)
    return Line3(anchor=point, direction=direction)
