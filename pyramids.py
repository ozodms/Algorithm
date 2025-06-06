# In this file we collect from the coordinates given in data.py and form a complete list of vertices to be rendered

# importing all coordinates from data.py
from data import (
    v1,
    v2_base, v2_apex,
    v3_base, v3_apex,
    v4_base, v4_apex,
    v5_base, v5_apex
)

faces = []

# lightblue pyramid
faces += [
    [v1[0], v1[1], v1[4]],
    [v1[1], v1[2], v1[4]],
    [v1[2], v1[3], v1[4]],
    [v1[3], v1[0], v1[4]],
    [v1[0], v1[1], v1[2], v1[3]]
]

# orange pyramid
faces += [
    [v2_base[0], v2_base[1], v2_apex],
    [v2_base[1], v2_base[2], v2_apex],
    [v2_base[2], v2_base[3], v2_apex],
    [v2_base[3], v2_base[0], v2_apex],
    [v2_base[0], v2_base[1], v2_base[2], v2_base[3]]
]

# lightgreen pyramid
faces += [
    [v3_base[0], v3_base[1], v3_apex],
    [v3_base[1], v3_base[2], v3_apex],
    [v3_base[2], v3_base[3], v3_apex],
    [v3_base[3], v3_base[0], v3_apex],
    [v3_base[0], v3_base[1], v3_base[2], v3_base[3]]
]

# violet pyramid
faces += [
    [v4_base[0], v4_base[1], v4_apex],
    [v4_base[1], v4_base[2], v4_apex],
    [v4_base[2], v4_base[3], v4_apex],
    [v4_base[3], v4_base[0], v4_apex],
    [v4_base[0], v4_base[1], v4_base[2], v4_base[3]]
]

# gold pyramid
faces += [
    [v5_base[0], v5_base[1], v5_apex],
    [v5_base[1], v5_base[2], v5_apex],
    [v5_base[2], v5_base[3], v5_apex],
    [v5_base[3], v5_base[0], v5_apex],
    [v5_base[0], v5_base[1], v5_base[2], v5_base[3]]
]

# colors for 25 faces
colors = (
    ['lightblue'] * 5 +
    ['orange'] * 5 +
    ['lightgreen'] * 5 +
    ['violet'] * 5 +
    ['gold'] * 5
)

# Here we collect all the vertices of all five pyramids into one even list to then draw them with red dots.
all_vertices = (
    v1[:4] + [v1[4]] +
    v2_base + [v2_apex] +
    v3_base + [v3_apex] +
    v4_base + [v4_apex] +
    v5_base + [v5_apex]
)