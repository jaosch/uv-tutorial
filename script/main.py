# /// script
# requires-python = ">=3.13"
# dependencies = ["numpy", "matplotlib"]
# ///

"""This is an exemplary standalone python script.

The dependencies required for running the script are specified in the header
comment above. The script can be run directly using the following command

```
uv run main.py
```

without the need for any manual package installation.

"""

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
