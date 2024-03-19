import numpy as np
import matplotlib.pyplot as plt

# Camera parameters for KB4
params_kb4 = [622, 622, 965, 631, -0.256, -0.0015, 0.0007, -0.0002]
fx, fy, cx, cy, k1, k2, k3, k4 = params_kb4
width, height = 1920, 1200

# Generate a grid of points
x = np.linspace(0, width, 50)
y = np.linspace(0, height, 30)
x, y = np.meshgrid(x, y)

# Normalize coordinates
x_norm = (x - cx) / fx
y_norm = (y - cy) / fy

r = np.sqrt(x_norm**2 + y_norm**2)
theta = np.arctan(r)

# Apply KB4 distortion
theta_d = theta * (1 + k1*theta**2 + k2*theta**4 + k3*theta**6 + k4*theta**8)
x_distorted = (theta_d / r) * x_norm * fx + cx
y_distorted = (theta_d / r) * y_norm * fy + cy

# Visualization
plt.figure(figsize=(10, 6))
plt.subplot(1, 2, 1)
plt.scatter(x, y, color='blue', label='Original')
plt.title('Original Grid')
plt.axis('equal')

plt.subplot(1, 2, 2)
plt.scatter(x_distorted, y_distorted, color='red', label='Distorted')
plt.title('Distorted Grid (KB4)')
plt.axis('equal')

plt.show()
