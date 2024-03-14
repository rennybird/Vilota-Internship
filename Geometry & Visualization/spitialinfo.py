import numpy as np
from spatialmath import SE3
from math import pi
import matplotlib.pyplot as plt

Ha = SE3.RPY([45, 60, 75], unit='deg') # Use Roll Pitch Yaw by Roll 45 degree, Pitch 60 degree, and Yaw 75 degree
Hb = SE3(1, 2, 3) * SE3.Rx(40, 'deg') * SE3.Ry(60, 'deg') * SE3.Rz(80, 'deg') # Move 1 unit along x, Move 2 unit along y, and Move 3 unit along z then Rotate 40 degree in x-axis, Rotate 60 degree in y-axis, and Rotate 80 degree in z-axis. But In this case Moving x y z are done in single command and then we Rotating .
Hc = SE3.Tx(1) * SE3.Ty(2) * SE3.Tz(-2.0) * SE3.Rx(40, 'deg')* SE3.Ry(60, 'deg')* SE3.Rz(80, 'deg') # Move 1 unit along x, Move 2 unit along y, and Move -2 unit along z then Rotate 40 degree in x-axis, Rotate 60 degree in y-axis, and Rotate 80 degree in z-axis. But In this we construch each transformation  then compose these translations with * and last we Rotating .
Hd = Hb * Hc # I combine Hb and Hc transformation by First move the object by (1, 2, 3) units then Rotate 40 degree in x-axis, Rotate 60 degree in y-axis, and Rotate 80 degree in z-axis. After that we move X for 1 more unit Y for 2 more unit and Z for -2 unit and lastly we Rotate 40 degree in x-axis, Rotate 60 degree in y-axis, and Rotate 80 degree in z-axis.
He = Hc.inv() # Inverse of Hc transformation so the it will move -1 unit along x, -2 unit along y, and 2 unit along z then Rotate -40 degree in x-axis, Rotate -60 degree in y-axis, and Rotate -80 degree in z-axis.



# Create plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.set_xlim([0, 4])
ax.set_ylim([0, 4])
ax.set_zlim([0, 4])
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Plot 
Ha.plot(ax=ax, frame='A', color='black')
Hb.plot(ax=ax, frame='B', color='red')
Hc.plot(ax=ax, frame='C', color='green')
Hd.plot(ax=ax, frame='D', color='blue')
He.plot(ax=ax, frame='E', color='cyan')
plt.show()
