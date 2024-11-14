import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Constants for projectile motion
g = 9.81  # Acceleration due to gravity (m/s^2)
v0 = 300  # Initial horizontal velocity (m/s)
y0 = 1.5  # Initial height of the bullet (meters)
t_max = 2 * np.sqrt(2 * y0 / g)  # Estimated max time for the projectile to hit the ground

# Time array for plotting
t = np.linspace(0, t_max, num=200)

# Projectile motion equations
x = v0 * t  # Horizontal position as a function of time (constant velocity)
y = y0 - 0.5 * g * t**2  # Vertical position as a function of time (accelerated motion)

# Filter only the points where y >= 0 (above ground)
x = x[y >= 0]
y = y[y >= 0]

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, max(x) * 1.1)
ax.set_ylim(0, max(y) * 1.1)
ax.set_xlabel("Horizontal Distance (m)")
ax.set_ylabel("Vertical Distance (m)")
ax.set_title("Bullet Projectile Motion")

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
    trajectory_line.set_data(x[:i], y[:i])
    bullet_dot.set_data(x[i], y[i])
    return trajectory_line, bullet_dot

# Create animation
ani = animation.FuncAnimation(fig, animate, frames=len(x), init_func=init, interval=30, blit=True)

# Save as a gif file
ani.save("bullet_projectile_motion.gif", writer='imagemagick', fps=30)