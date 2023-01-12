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

    Set of plane points is defined by the equation: (normalized_normal, x) = distance.
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

    Set of line points is defined by the equation: anchor + direction * t = x
    Set of plane points is defined by the equation: (normalized_normal, x) = distance

    Substitution of x gives
    (normalized_normal, anchor) + (normalized_normal, direction) * t = distance
    t = (distance - (normalized_normal, anchor)) / (normalized_normal, direction)

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
    (normal, line_1_point) = distance_1 - plane that contains line 1.
    (normal, line_2_point) = distance_2 - plane that contains line 2.
    (normal, line_1_point - line_2_point) - distance between planes.

    If lines are collinear then take distance from point of one line to other line.
    '''
    normal = norm3(cross3(a_line.direction, b_line.direction))
    if is_zero3(normal):
        return point_line_distance(a_line.anchor, b_line)
    return abs(dot3(normal, sub3(a_line.anchor, b_line.anchor)))
