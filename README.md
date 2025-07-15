# UV Tutorial – Python Project

This repository contains sample scripts for visualizing mathematical functions using Python, structured using the `uv` package manager and organized with the modern `pyproject.toml` format.



##  Setup Instructions

1. **Install [uv](https://github.com/astral-sh/uv):**  
   If not installed, follow the instructions from the [uv GitHub page](https://github.com/astral-sh/uv).

2. **Install Dependencies:**
uv add numpy matplotlib

3. Run scripts
```bash
uv run scripts/tutorial1.py
uv run scripts/tutorial2_1.py
uv run scripts/tutorial2_2.py
```
## Tutorial 1 – Square Function Plot
A simple plot of the function:

\[
y = x^2
\]

File: scripts/tutorial1.py
* Command 
```bash
uv run scripts/tutorial1.py
```
# Uses:
* numpy to generate x values *
* matplotlib for plotting
* A square function defined directly in the script

## Tutorial 2 – Reusable Modules
Demonstrates how to write reusable plotting functions in your own modules and import them into scripts.

Modules in src/myproject/:

* sinutil.py: defines sine_wave()
* cubic_util.py: defines cubic()

# Sine Wave Plot (tutorial2_1.py)

* Plots:  
  \[
  y = sin(x)
  \]

* Uses `sinutil.py` module from `src/myproject/`.

* Command:
```bash
uv run scripts/tutorial2_1.py
```

# Cubic Function Plot (tutorial2_2.py)

* Plots:  
  \[
  y = x^3
  \]
* Uses `cubic_util.py` module from `src/myproject/`.

* Command:
```bash
uv run scripts/tutorial2_2.py
```
## Notes

* The project uses a src/ layout, enabled via the pyproject.toml section:

* All reusable logic is inside src/myproject/ and can be imported like:

from myproject import sinutil

* Python version is pinned using the .python-version file:

3.11
This ensures consistent Python versions across collaborators.

* Dependencies are declared in pyproject.toml and locked in uv.lock. You can add a dependency like:
```bash
uv add numpy
```
* All code can be run via uv run, which handles virtual environments automatically:
```bash
uv run scripts/tutorial1.py
```
* You can lock your script's dependencies for reproducibility:
```bash
uv lock --script scripts/tutorial1.py
```
