from .vec3 import Vec3, add3, sub3, len3, project3
from .line3 import Line3

def point_line_projection(point: Vec3, line: Line3) -> Vec3:
    '''Projects point on line.

    For an arbitrary line point project vector from that point to target point onto line.
    Offset line point by that projection.
    '''
    anchor_to_point_dir = sub3(point, line.anchor)
    anchor_to_point_proj = project3(anchor_to_point_dir, line.direction)
    return add3(line.anchor, anchor_to_point_proj)

def point_line_distance(point: Vec3, line: Line3) -> float:
    '''Finds distance from point to line.

    Take distance between target point and its projection onto line.
    '''
    point_proj = point_line_projection(point, line)
    return len3(sub3(point, point_proj))
