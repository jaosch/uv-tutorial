import numpy as np
import matplotlib.pyplot as plt
from myproject import cubic_util  # importing the new module

x = np.linspace(-10, 10, 200)
y = cubic_util.cubic(x)

plt.plot(x, y)
plt.title("Cubic Function: y = x³")
plt.xlabel("x")
plt.ylabel("y = x³")
plt.grid(True)
plt.show()
