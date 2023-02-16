'''
Yong Da Li
Friday, February 10, 2023

polar plots for ECE422 lab 1
'''

import numpy as np
import matplotlib.pyplot as plt

# change the theory calculations as needed
theta_theory = np.arange(0, 2*np.pi, 0.01)
# r_theory = np.sin(theta_theory)
# r_theory = ( (np.cos(np.pi/2 * np.cos(theta_theory))) / (np.sin(theta_theory)) )**2
r_theory = 1.0* np.ones(len(theta_theory))     # constant

filename = "dipole_hplane.txt"
theta = []
val = []
with open(filename, "r") as f:
    line = f.read().split("\n")
    for elem in line:
        theta.append(float(elem.split("\t")[0]))
        val.append(float(elem.split("\t")[1]))
        

# convert theta to radians
theta = np.array(theta)
theta = ((theta+90)%360) * np.pi / 180  # our measurement started at max power (this should be theta = 90)

# raise so min value is 0, and normalize
val = np.array(val)
val_raised = val - min(val) + 10

val_norm = val_raised / max(val_raised)

# ====== debugging ==========
# print("==== this is what is being plotted after normalizing and re-orienting ====")
# for i, (x, y) in enumerate(zip(theta, val_norm)):
#     print("{:2d}, {:f}, {:f}".format( i, x, y))

fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
ax.scatter(theta, val_norm, label="experiment")
ax.plot(theta_theory, r_theory, color='orange', label="theory")
ax.set_theta_zero_location("N")
ax.set_theta_direction(-1)  # theta increasing clockwise


# ax.set_rmax(2)
ax.set_rticks([0.5, 1.0])  # Less radial ticks
# ax.set_rlabel_position(-22.5)  # Move radial labels away from plotted line
ax.grid(True)
ax.legend()
ax.set_title(filename, va='bottom')
plt.savefig("plots/" + filename.replace("txt", "png"))
# plt.show()
