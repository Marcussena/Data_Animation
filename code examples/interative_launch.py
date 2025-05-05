import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Slider

# --- Constants ---
g = 9.81  # gravity

# --- Initial Parameters ---
v0_init = 20
theta_init = 45  # in degrees

# --- Figure and Axes Setup ---
fig, ax = plt.subplots()
plt.subplots_adjust(left=0.1, bottom=0.25)  # space for sliders

# Initialize empty plots
line, = ax.plot([], [], lw=2)
point, = ax.plot([], [], 'ro')

# Set fixed axis limits (can be adjusted later dynamically)
ax.set_xlim(0, 50)
ax.set_ylim(0, 30)
ax.set_title("Oblique Launch (Interactive)")
ax.set_xlabel("Distance")
ax.set_ylabel("Height")

# --- Sliders Setup ---
ax_angle = plt.axes([0.1, 0.15, 0.8, 0.03])
ax_velocity = plt.axes([0.1, 0.1, 0.8, 0.03])

angle_slider = Slider(ax_angle, 'Angle (°)', 0, 90, valinit=theta_init)
velocity_slider = Slider(ax_velocity, 'Velocity (m/s)', 1, 50, valinit=v0_init)

# --- Compute Trajectory ---
def compute_trajectory(v0, theta_deg):
    theta = np.radians(theta_deg)
    t_flight = 2 * v0 * np.sin(theta) / g
    t = np.linspace(0, t_flight, 100)
    x = v0 * np.cos(theta) * t
    y = v0 * np.sin(theta) * t - 0.5 * g * t**2
    return x, y

x, y = compute_trajectory(v0_init, theta_init)

# --- Init Function for Animation ---
def init():
    line.set_data([], [])
    point.set_data([], [])
    return line, point

# --- Update Function for Animation ---
def update(frame):
    global x, y
    if frame < len(x):
        line.set_data(x[:frame], y[:frame])
        point.set_data(x[frame], y[frame])
    return line, point

# --- Create Animation ---
ani = FuncAnimation(fig, update, frames=100, init_func=init, blit=True, interval=30)

# --- Slider Event Callback ---
def update_sliders(val):
    global x, y
    v0 = velocity_slider.val
    theta = angle_slider.val
    x, y = compute_trajectory(v0, theta)
    ax.set_xlim(0, max(x)*1.1)
    ax.set_ylim(0, max(y)*1.1)
    init()

angle_slider.on_changed(update_sliders)
velocity_slider.on_changed(update_sliders)

plt.show()
