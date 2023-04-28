import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint

plt.style.use("seaborn-darkgrid")

# For reproducibility
np.random.seed(20394)


def freefall(y, t, p):
    return 2.0 * p[1] - p[0] * y[0]


# Times for observation
times = np.arange(0, 10, 0.5)
gamma, g, y0, sigma = 0.4, 9.8, -2, 2
y = odeint(freefall, t=times, y0=y0, args=tuple([[gamma, g]]))
yobs = np.random.normal(y, 2)

fig, ax = plt.subplots(dpi=120)
plt.plot(times, yobs, label="observed speed", linestyle="dashed", marker="o", color="red")
plt.plot(times, y, label="True speed", color="k", alpha=0.5)
plt.legend()
plt.xlabel("Time (Seconds)")
plt.ylabel(r"$y(t)$")
plt.show()

