import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

x = np.linspace(0, 2 * np.pi, 1000)
y = np.sin(x)

fig, ax = plt.subplots()
line, = ax.plot(x, y)

ax.set_ylim(-1.5, 1.5)

# Update function for animation
def update(frame):
    line.set_ydata(np.sin(x + frame / 10))
    return line,

ani = FuncAnimation(fig, update, frames=300, interval=50, blit=True)
plt.show()

ani.save("sine_wave.gif", writer='pillow')