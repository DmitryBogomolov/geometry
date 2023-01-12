from .vec3 import Vec3, add3, sub3, len3, project3
from .line3 import Line3

def project_point_line(point: Vec3, line: Line3) -> Vec3:
    anchor_to_point_dir = sub3(point, line.anchor)
    anchor_to_point_proj = project3(anchor_to_point_dir, line.direction)
    return add3(line.anchor, anchor_to_point_proj)

def point_line_distance(point: Vec3, line: Line3) -> float:
    point_proj = project_point_line(point, line)
    return len3(sub3(point, point_proj))
