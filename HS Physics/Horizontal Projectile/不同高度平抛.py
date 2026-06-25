import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.patches import FancyArrowPatch

# Constants for projectile motion
g = 10  # Acceleration due to gravity (m/s^2)
v0 = 300  # Initial horizontal velocity (m/s)

# Different heights and their corresponding colors
heights = [9, 18, 36]
colors = ['b', 'g', 'r']
labels = [f"h = {h} m" for h in heights]

# Create time arrays for each height based on free-fall time
t_values = [np.linspace(0, np.sqrt(2 * h / g), num=200) for h in heights]

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, v0 * max(t_values[-1]) * 1.1)  # Adjust x-axis to longest projectile range
ax.set_ylim(0, max(heights) * 1.1)  # Adjust y-axis to fit highest height
ax.invert_yaxis()  # Invert y-axis for projectile motion
ax.set_xlabel("Horizontal Distance (m)")
ax.set_ylabel("Vertical Distance (m)")
ax.set_title("Trajectories of Projectiles from Different Heights")

# Adding arrows for axes
ax.add_patch(FancyArrowPatch((0, 0), (v0 * max(t_values[-1]) * 1.1, 0), mutation_scale=15, color="black"))
ax.add_patch(FancyArrowPatch((0, 0), (0, max(heights) * 1.1), mutation_scale=15, color="black"))

# Initialize lists for trajectory lines and bullet dots for each height
trajectory_lines = []
bullet_dots = []

# Create lines and dots for each projectile height and add to lists
for color, label in zip(colors, labels):
    line, = ax.plot([], [], '--', color=color, lw=2, label=label)
    dot, = ax.plot([], [], 'o', color=color, markersize=6)
    trajectory_lines.append(line)
    bullet_dots.append(dot)

# Add legend to distinguish each height
ax.legend()

# Initialization function for the animation
def init():
    for line, dot in zip(trajectory_lines, bullet_dots):
        line.set_data([], [])
        dot.set_data([], [])
    return trajectory_lines + bullet_dots

# Animation function
def animate(i):
    # Update the position of each projectile based on its time array
    for idx, (h, t, line, dot) in enumerate(zip(heights, t_values, trajectory_lines, bullet_dots)):
        x = v0 * t  # Horizontal position as a function of time
        y = 0.5 * g * t**2  # Vertical position as a function of time
        # Plot up to the current frame i, with conditional length to handle different t array lengths
        line.set_data(x[:min(i, len(x)-1)], y[:min(i, len(y)-1)])
        dot.set_data([x[min(i, len(x)-1)]], [y[min(i, len(y)-1)]])
    return trajectory_lines + bullet_dots

# Create animation
ani = animation.FuncAnimation(fig, animate, frames=len(t_values[-1]), init_func=init, interval=10, blit=True)

# Save as a video (mp4 format) using ffmpeg
ani.save("Projectiles_from_Different_Heights.mp4", writer='ffmpeg', fps=60, dpi=300)