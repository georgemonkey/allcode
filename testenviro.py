import numpy as np
import matplotlib.pyplot as plt

# Define cam rotation angles (degrees)
theta = np.linspace(0, 360, 361)

# Create an idealized displacement model (can be replaced with actual cam profile data)
# Example motion phases: rise (0–90), dwell (90–180), fall (180–270), dwell (270–360)
displacement = []

for angle in theta:
    if 0 <= angle < 90:
        # Rise: follower rises smoothly (parabolic)
        h = 10 * (1 - np.cos(np.radians(angle))) / 2
    elif 90 <= angle < 180:
        # Dwell: constant height
        h = 10
    elif 180 <= angle < 270:
        # Fall: follower returns
        h = 10 * (1 + np.cos(np.radians(angle - 180))) / 2
    else:
        # Dwell: back to base
        h = 0
    displacement.append(h)

# Plotting the displacement diagram
plt.figure(figsize=(10, 5))
plt.plot(theta, displacement, label='Follower Displacement', color='blue')
plt.title("aashi cam follower graph")
plt.xlabel("Cam Angle (degrees)")
plt.ylabel("Follower Displacement (mm)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
