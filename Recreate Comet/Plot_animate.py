import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter
from Orbit_sim import sim_orbit_Newton

x_vals, y_vals = sim_orbit_Newton()

#figure and axis
fig, ax = plt.subplots(figsize=(8,8))
ax.set_xlim(-6e12,6e12)
ax.set_ylim(-6e12,6e12)
ax.set_aspect('equal')
ax.grid()

#plot
sun = ax.plot(0,0,'yo', markersize=10)[0]
comet, = ax.plot([],[],'bo',label="Halley's Comet")
trail, = ax.plot([],[],'b-', alpha=0.5)

def init():
    comet.set_data([],[])
    trail.set_data([],[])
    return comet, trail

def update(frame):
    comet.set_data(x_vals[frame],y_vals[frame])
    trail.set_data(x_vals[:frame],y_vals[:frame])
    return comet, trail

frame_skip = 5000
frames = range(0,len(x_vals), frame_skip)
animate = FuncAnimation(fig,update,frames=frames, interval=30, blit=True)

plt.title("Animated Orbit")
ax.legend()

# animate.save("Recreate Comet/Images/Halley_Orbit_animated.gif", writer=PillowWriter(fps=30))

plt.show()