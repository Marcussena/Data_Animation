import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Parameters
g = 9.81  # gravity (m/s^2)
v0 = 20   # initial velocity (m/s)
theta = np.radians(45)  # launch angle

# Time vector
t_flight = 2 * v0 * np.sin(theta) / g
t = np.linspace(0, t_flight, 100)

# Equations of motion
x = v0 * np.cos(theta) * t
y = v0 * np.sin(theta) * t - 0.5 * g * t**2

# Set up the plot
fig, ax = plt.subplots()
ax.set_xlim(0, max(x)*1.1)
ax.set_ylim(0, max(y)*1.1)
ax.set_title("Oblique Launch")
ax.set_xlabel("Distance")
ax.set_ylabel("Height")
line, = ax.plot([], [], lw=2)
point, = ax.plot([], [], 'ro')  # red dot for projectile

# Initialize plot elements
def init():
    line.set_data([], [])
    point.set_data([], [])
    return line, point

# Animation function
def update(frame):
    line.set_data(x[:frame], y[:frame])
    point.set_data(x[frame], y[frame])
    return line, point

ani = FuncAnimation(fig, update, frames=len(t), init_func=init, blit=True, interval=30)

# Export as GIF (optional)
ani.save("launch.gif", writer='pillow', fps=30)
plt.show()
