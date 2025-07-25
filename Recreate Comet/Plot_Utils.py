import matplotlib.pyplot as plt

def plot_orbit(x,y, title):
    plt.figure(figsize=(8,8))
    plt.plot(x, y, label="Halley's Comet")
    plt.plot(0, 0, 'yo', label="Sun")  # Sun at origin
    plt.xlabel('x (m)')
    plt.ylabel('y (m)')
    plt.title(title)
    plt.legend()
    plt.grid(True)
    plt.axis('equal')  # Keep aspect ratio square
    plt.xlim(-6e12, 6e12)
    plt.ylim(-6e12, 6e12)
    plt.show()