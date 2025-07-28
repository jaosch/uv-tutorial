import numpy as np
import matplotlib.pyplot as plt
from myproject import sinutil # import your module

x = np.linspace(0, 2 * np.pi, 100)
y = sinutil.sine_wave(x)

plt.plot(x, y)
plt.title("Sine Wave")
plt.xlabel("x (radians)")
plt.ylabel("sin(x)")
plt.grid(True)
plt.show()
