
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from pyramids import faces, colors, all_vertices

def main():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    for i, face in enumerate(faces):
        ax.add_collection3d(
            Poly3DCollection(
                [face],
                facecolors=colors[i],
                linewidths=1,
                edgecolors='black',
                alpha=0.7
            )
        )

    # drawing each verse with red point
    x, y, z = zip(*all_vertices)
    ax.scatter(x, y, z, color='red')

    # graphic set up
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_xlim(0, 6)
    ax.set_ylim(0, 5)
    ax.set_zlim(0, 4)
    ax.grid(True)

    plt.title("Ozodbek M")
    plt.show()

if __name__ == "__main__":
    main()