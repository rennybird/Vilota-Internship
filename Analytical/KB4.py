import numpy as np
import matplotlib.pyplot as plt

fx, fy, cu, cv, k1, k2, k3, k4 = [622, 622, 865, 631, -0.256, -0.0015, 0.0007, -0.0002]

def distort(x, y, fx, fy, cu, cv, k1, k2, k3, k4):
    
    x_norm = (x - cu) / fx
    y_norm = (y - cv) / fy
    
    
    r2 = x_norm**2 + y_norm**2
    r4 = r2**2
    r6 = r4 * r2
    
    distortion_factor = 1 + k1 * r2 + k2 * r4 + k3 * r6 + k4 * r4 * r2
    x_distorted = x_norm * distortion_factor
    y_distorted = y_norm * distortion_factor
    
    x_distorted = x_distorted * fx + cu
    y_distorted = y_distorted * fy + cv
    
    return x_distorted, y_distorted

width, height = 1920, 1080
step_size = 50
x_grid, y_grid = np.meshgrid(np.arange(0, width, step_size), np.arange(0, height, step_size))

x_distorted, y_distorted = distort(x_grid, y_grid, fx, fy, cu, cv, k1, k2, k3, k4)

plt.figure(figsize=(10, 6))
plt.quiver(x_grid, y_grid, x_distorted - x_grid, y_distorted - y_grid, angles='xy', scale_units='xy', scale=1, color='r', width=0.005)
plt.title('Distortion')
plt.xlim([0, width])
plt.ylim([height, 0])
plt.xlabel('X Pixel')
plt.ylabel('Y Pixel')
plt.grid(True)
plt.show()
