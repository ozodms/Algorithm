import numpy as np
import math
import gdist
from collections import defaultdict

from data import vertices, faces, start_idx, target_idx

def euclidean_distance(p1, p2):
    return math.sqrt(np.sum((p1 - p2) ** 2))

def ray_triangle_intersect(origin, direction, v0, v1, v2, eps=1e-6):
    edge1 = v1 - v0
    edge2 = v2 - v0
    h = np.cross(direction, edge2)
    a = np.dot(edge1, h)
    if abs(a) < eps:
        return None
    f = 1.0 / a
    s = origin - v0
    u = f * np.dot(s, h)
    if u < 0.0 or u > 1.0:
        return None
    q = np.cross(s, edge1)
    v = f * np.dot(direction, q)
    if v < 0.0 or u + v > 1.0:
        return None
    t = f * np.dot(edge2, q)
    if t > eps:
        intersection_point = origin + direction * t
        return intersection_point, t
    return None

start_point = vertices[start_idx]
target_point = vertices[target_idx]

direct_distance = euclidean_distance(start_point, target_point)

source_indices = np.array([start_idx], dtype=np.int32)
distances = gdist.compute_gdist(vertices, faces, source_indices)
geodesic_distance = distances[target_idx]

neighbors = defaultdict(set)
for triangle in faces:
    a, b, c = triangle
    neighbors[a].update([b, c])
    neighbors[b].update([a, c])
    neighbors[c].update([a, b])

path = [target_idx]
current = target_idx
while current != start_idx:
    current_dist = distances[current]
    next_vertex = min(neighbors[current], key=lambda n: distances[n])
    if distances[next_vertex] >= current_dist:
        break
    path.append(next_vertex)
    current = next_vertex
path = path[::-1]
geodesic_path = vertices[path]

num_samples = 200
max_z = vertices[:, 2].max() + 1.0
orange_path = []
for t in np.linspace(0, 1, num_samples):
    point_on_line = start_point + t * (target_point - start_point)
    ray_origin = np.array([point_on_line[0], point_on_line[1], max_z])
    ray_direction = np.array([0.0, 0.0, -1.0])
    best_hit, min_t = None, float('inf')
    for triangle in faces:
        a, b, c = vertices[triangle]
        result = ray_triangle_intersect(ray_origin, ray_direction, a, b, c)
        if result is not None and result[1] < min_t:
            best_hit, min_t = result
    if best_hit is None:
        best_hit = np.array([point_on_line[0], point_on_line[1], 0.0])
    orange_path.append(best_hit)
orange_path = np.array(orange_path)

orange_distance = sum(
    euclidean_distance(orange_path[i], orange_path[i+1])
    for i in range(len(orange_path) - 1)
)