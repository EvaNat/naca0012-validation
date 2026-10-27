import numpy as np
import matplotlib.pyplot as plt

v = np.linspace(0, 100, 200)                        # speed m/s
q = 0.5 * 1.225 * v**2

plt.plot(v, q)
plt.xlabel("Speed (m/s)")
plt.ylabel("Dynamic Pressure (Pa)")
plt.title("dynamic pressure vs speed")
plt.savefig("results/test_plot.png", dpi=150)
