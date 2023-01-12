from .vec3 import Vec3, add3, sub3, mul3, len3, project3, norm3
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
    '''
    # Set of plane points is defined by the equation: (normal, x) = distance.
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
