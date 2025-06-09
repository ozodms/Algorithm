import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

from data import vertices, faces, start_idx, target_idx
from pyramids import direct_distance, geodesic_distance, geodesic_path, orange_path, orange_distance

def main():
    print(f"Euclidean distance: {direct_distance:.4f}")
    print(f"Geodesic distance over surface: {geodesic_distance:.4f}")
    print(f"Length of projected path: {orange_distance:.4f}")

    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection='3d')

    for triangle in faces:
        triangle_pts = [vertices[i] for i in triangle]
        ax.add_collection3d(Poly3DCollection(
            [triangle_pts],
            facecolors='lightgray',
            linewidths=0.5,
            edgecolors='black',
            alpha=0.3
        ))

    ax.scatter(vertices[:, 0], vertices[:, 1], vertices[:, 2], color='gray', s=30)
    ax.scatter(*vertices[start_idx], color='blue', s=100, label=f'Start {vertices[start_idx]}')
    ax.scatter(*vertices[target_idx], color='red', s=100, label=f'Target {vertices[target_idx]}')

    ax.plot(
        [vertices[start_idx][0], vertices[target_idx][0]],
        [vertices[start_idx][1], vertices[target_idx][1]],
        [vertices[start_idx][2], vertices[target_idx][2]],
        linestyle='--', linewidth=2, label=f'Euclidean = {direct_distance:.2f}'
    )

    ax.plot(
        geodesic_path[:, 0], geodesic_path[:, 1], geodesic_path[:, 2],
        linewidth=3, label=f'Geodesic = {geodesic_distance:.2f}'
    )

    ax.plot(
        orange_path[:, 0], orange_path[:, 1], orange_path[:, 2],
        linewidth=2, label=f'Projected = {orange_distance:.2f}'
    )

    ax.set_xlabel("X axis")
    ax.set_ylabel("Y axis")
    ax.set_zlabel("Z axis")
    ax.set_title("Comparison of Three Paths")
    ax.legend(loc='upper left', fontsize=9)
    ax.view_init(elev=20, azim=45)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()