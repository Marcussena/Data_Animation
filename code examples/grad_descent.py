import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the function and its gradient
def f(x, y):
    return x**2 + y**2

def grad_f(x, y):
    return 2*x, 2*y

# Initialize parameters
lr = 0.1
steps = 50
x, y = 4.0, 4.0  # start point
history = [(x, y)]

# Perform gradient descent
for _ in range(steps):
    dx, dy = grad_f(x, y)
    x -= lr * dx
    y -= lr * dy
    history.append((x, y))

# Extract coordinates
xs, ys = zip(*history)
zs = [f(xi, yi) for xi, yi in history]

# Prepare 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
X, Y = np.meshgrid(np.linspace(-5, 5, 100), np.linspace(-5, 5, 100))
Z = f(X, Y)
ax.plot_surface(X, Y, Z, alpha=0.6, cmap='viridis')
point, = ax.plot([], [], [], 'ro', markersize=6)
line, = ax.plot([], [], [], 'r-', lw=1)

# Animation functions
def init():
    point.set_data([], [])
    point.set_3d_properties([])
    line.set_data([], [])
    line.set_3d_properties([])
    return point, line

def update(i):
    point.set_data(xs[i], ys[i])
    point.set_3d_properties(zs[i])
    line.set_data(xs[:i+1], ys[:i+1])
    line.set_3d_properties(zs[:i+1])
    return point, line

ani = FuncAnimation(fig, update, frames=len(xs), init_func=init, blit=True, interval=200)

# Optional: Save or just show
ani.save("gradient_descent.gif", writer="pillow")
plt.show()
