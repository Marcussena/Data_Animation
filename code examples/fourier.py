import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Create time values
x = np.linspace(-np.pi, np.pi, 1000)
y = np.zeros_like(x)

# Initialize plot
fig, ax = plt.subplots()
line, = ax.plot(x, y, lw=2)
ax.set_title("Fourier Series Approximation of a Square Wave")
ax.set_ylim(-1.5, 1.5)
ax.set_xlim(-np.pi, np.pi)
text = ax.text(-np.pi, 1.3, '', fontsize=12)

# Fourier series parameters
def fourier_series(n_terms):
    result = np.zeros_like(x)
    for n in range(1, n_terms * 2, 2):  # only odd harmonics
        result += (4 / (np.pi * n)) * np.sin(n * x)
    return result

# Animation update function
def update(frame):
    y = fourier_series(frame + 1)
    line.set_ydata(y)
    text.set_text(f'{2*frame+1} terms')
    return line, text

ani = FuncAnimation(fig, update, frames=20, interval=200, blit=True)

# Optional: Save as gif or mp4
ani.save('fourier_series.gif', writer='imagemagick', fps=30)
plt.show()
