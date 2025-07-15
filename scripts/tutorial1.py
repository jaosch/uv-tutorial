# /// script
# dependencies = ["numpy", "matplotlib"]
# ///

import numpy as np
import matplotlib.pyplot as plt

def square(x):
    return x * x

x = np.linspace(0, 10, 100)
y = square(x)

plt.plot(x, y)
plt.title("Plot of y = x²")
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.show()
