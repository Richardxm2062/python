import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.patches import FancyArrowPatch

# Constants for projectile motion
g = 10  # Acceleration due to gravity (m/s^2)
y0 = 0  # Initial height of the bullet (meters)
h = 18  # Height limit for the y-axis
v_values = [200, 300, 400]  # Different initial horizontal velocities
colors = ['b', 'g', 'r']  # Colors for each projectile
labels = [f"v0 = {v} m/s" for v in v_values]  # Labels for legend

# Determine the max time based on the height (for uniform time axis)
t_max = np.sqrt(2 * h / g)
t = np.linspace(0, t_max, num=200)  # Time array for plotting

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, max(v_values) * t_max * 1.1)
ax.set_ylim(0, h)  # Adjust the vertical axis to fit the height limit of 18 meters
ax.invert_yaxis()  # Invert y-axis for projectile motion
ax.set_xlabel("Horizontal Distance (m)")
ax.set_ylabel("Vertical Distance (m)")
ax.set_title("Comparative Trajectories of Horizontal Projectiles at Different Speeds")

# Adding arrows for axes
ax.add_patch(FancyArrowPatch((0, 0), (max(v_values) * t_max * 1.1, 0), mutation_scale=15, color="black"))
ax.add_patch(FancyArrowPatch((0, 0), (0, h), mutation_scale=15, color="black"))

# Initialize lists for trajectory lines and bullet dots for each velocity
trajectory_lines = []
bullet_dots = []

# Create lines and dots for each projectile and add to lists
for color, label in zip(colors, labels):
    line, = ax.plot([], [], '--', color=color, lw=2, label=label)
    dot, = ax.plot([], [], 'o', color=color, markersize=6)
    trajectory_lines.append(line)
    bullet_dots.append(dot)

# Add legend to distinguish each velocity
ax.legend()

# Initialization function for the animation
def init():
    for line, dot in zip(trajectory_lines, bullet_dots):
        line.set_data([], [])
        dot.set_data([], [])
    return trajectory_lines + bullet_dots

# Animation function
def animate(i):
    # Update the position of each projectile for frame i
    for idx, (v0, line, dot) in enumerate(zip(v_values, trajectory_lines, bullet_dots)):
        x = v0 * t  # Horizontal position as a function of time (constant velocity)
        y = y0 + 0.5 * g * t**2  # Vertical position as a function of time (accelerated motion)
        line.set_data(x[:i], y[:i])  # Update the trajectory line up to frame i
        dot.set_data([x[i]], [y[i]])  # Update the position of the bullet dot
    return trajectory_lines + bullet_dots

# Create animation
ani = animation.FuncAnimation(fig, animate, frames=len(t), init_func=init, interval=10, blit=True)

# Save as a video (mp4 format) using ffmpeg
ani.save("Comparative_Trajectories_of_Horizontal_Projectiles.mp4", writer='ffmpeg', fps=60, dpi=300)