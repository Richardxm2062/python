import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.patches import FancyArrowPatch

# Constants for projectile motion
g = 10  # Acceleration due to gravity (m/s^2)
v0 = 400  # Initial horizontal velocity (m/s)
y0 = 0  # Initial height of the bullet (meters)
h = 18 # height
t_max = np.sqrt(2 * h / g)  # Estimated max time for the projectile to hit the ground

# Time array for plotting
t = np.linspace(0, t_max, num=200)

# Projectile motion equations
x = v0 * t  # Horizontal position as a function of time (constant velocity)
y = y0 + 0.5 * g * t**2  # Vertical position as a function of time (accelerated motion)


# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, max(x) * 1.2)
ax.set_ylim(0, max(y) * 1)  # Adjust the vertical axis to fit the new y range
ax.invert_yaxis()
ax.set_xlabel("Horizontal Distance (m)")
ax.set_ylabel("Vertical Distance (m)")
ax.set_title("Trajectory of Horizontal Projectile")

# Adding arrows for axes
# Horizontal arrow (right)
ax.add_patch(FancyArrowPatch((0, 0), (max(x)*1.2, 0), mutation_scale=15, color="black"))
# Vertical arrow (downward)
ax.add_patch(FancyArrowPatch((0, 0), (0, max(y)*1), mutation_scale=15, color="black"))


# Plot the trajectory line
trajectory_line, = ax.plot([], [], 'r--', lw=2)
bullet_dot, = ax.plot([], [], 'bo', markersize=6)

# Initialization function for the animation
def init():
    trajectory_line.set_data([], [])
    bullet_dot.set_data([], [])
    return trajectory_line, bullet_dot

# Animation function
def animate(i):
    # Set data for trajectory line up to current frame i
    trajectory_line.set_data(x[:i], y[:i])  # Keep the trajectory up to the ith point
    bullet_dot.set_data([x[i]], [y[i]])  # Pass a list containing the current x and y values
    return trajectory_line, bullet_dot

# Create animation
ani = animation.FuncAnimation(fig, animate, frames=len(x), init_func=init, interval=10, blit=True)

# Save as a video (mp4 format) using ffmpeg
ani.save("Trajectory of Horizontal Projectilen.mp4", writer='ffmpeg', fps=60, dpi=300)