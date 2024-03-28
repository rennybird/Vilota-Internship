import numpy as np
import matplotlib.pyplot as plt

fx, fy, cx, cy, k1, k2, k3, k4 = [622, 622, 965, 631, -0.256, -0.0015, 0.0007, -0.0002]

def distort_kb4(x, y, fx, fy, cx, cy, k1, k2, k3, k4):
    x_norm = (x - cx) / fx
    y_norm = (y - cy) / fy

    r = np.sqrt(x_norm**2 + y_norm**2)
    theta = np.arctan(r)

    theta_d = theta * (1 + k1*theta**2 + k2*theta**4 + k3*theta**6 + k4*theta**8)
    x_distorted = (theta_d / r) * x_norm * fx + cx
    y_distorted = (theta_d / r) * y_norm * fy + cy

    return x_distorted, y_distorted

width, height = 1920, 1200
step_size = 50

x_grid, y_grid = np.meshgrid(np.arange(0, width, step_size), np.arange(0, height, step_size))

x_distorted, y_distorted = distort_kb4(x_grid, y_grid, fx, fy, cx, cy, k1, k2, k3, k4)

fig, axs = plt.subplots(1, 2, figsize=(20, 10), gridspec_kw={'width_ratios': [1, 1]})

axs[0].scatter(x_grid, y_grid, color='blue')
axs[0].set_title('Original Grid')
axs[0].axis('equal')
axs[0].set_xlim([0, width])
axs[0].set_ylim([0, height])

axs[1].scatter(x_distorted, y_distorted, color='red')
axs[1].set_title('Distorted Grid (KB4)')
axs[1].axis('equal')
axs[1].set_xlim([0, width])
axs[1].set_ylim([0, height])
plt.show()
