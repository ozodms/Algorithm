#here we store all coordinates for five triangles

# lightblue pyramid
v1 = [
    (0, 0, 0),
    (2, 0, 0),
    (2, 3, 0),
    (0, 3, 0),
    (1, 1.5, 2)
]

# orange pyramid
v2_base = [
    v1[1],
    v1[2],
    (3, 3, 0),
    (3, 0, 0)
]
v2_apex = (3, 1.5, 3)

# lightgreen pyramid
v3_base = [
    v2_base[3],   # (3, 0, 0)
    v2_base[2],   # (3, 3, 0)
    (4, 3, 0),
    (4, 0, 0)
]
v3_apex = (4, 1.5, 2.5)

# violet pyramid
v4_base = [
    v1[3],        # (0, 3, 0)
    v1[2],        # (2, 3, 0)
    (2, 4, 0),
    (0, 4, 0)
]
v4_apex = (1, 3.5, 2.5)

# gold pyramid
v5_base = [
    (4, 0, 0),
    (4, 3, 0),
    (5, 3, 0),
    (5, 0, 0)
]
v5_apex = (5, 1.5, 2)