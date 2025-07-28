# UV Tutorial – Python Project

This repository contains an exemplary python project, structured using the `uv` package manager and declared with the modern `pyproject.toml` format. Its 
purpose is to showcase the usefullness of `uv` for creating reproducible python development environments for research and beyond.

**Note**: Most of the information provided in this repository is taken directly from the excellent
[uv documentation](https://github.com/astral-sh/uv), which should be the main source for any questions regarding the content of this project.

## Repository structure

In this repository we present three alternative approaches for creating reproducible
python project with `uv`. Complexity as well as code reusability increase in acending order. If you are building a large project, with a lot of reused code, 
the third alternative is certainly preferred in terms of maintainability.

1. `example_script`: A standalone uv python script, which declares all its dependencies in a header comment.
2. `example_application`: An exemplary python application, where all dependecies are specified in a `pyproject.toml` file and the code lies in a `main.py` file.
3. `example_library`: A python library, consisting of a package and script, which import the package.

## Installation

To be able to follow the steps below, make sure to **install** [`uv`](https://github.com/astral-sh/uv) and **clone** the present repository.

## Examples

### 1 .Standalone script - `script`

This script created simple plot of the function:

\[
y = x^2
\]

Its dependencies are `matplolib` and `numpy`, which are specified in the header comment of the `main.py` file. To run the script, enter the `script` directory and call

```bash
uv run main.py
```

By doing so, `uv` will automatically provide all required dependencies for you.
You should see a plot of the above function as a result.

You may lock your script's dependencies for reproducibility:
```bash
uv lock --script main.py
```


### 2. Application - `application`

Next, we present a simple application consisting of a `main.py` file inside the `application/scripts` directory and a `pyproject.toml`. The script implements and
plots a simple

\[
  y = sin(x)
\]

function. However, in contrast to the first example, the dependencies are not 
specified directly in the `main.py`, but in the `pyproject.toml` file. The main advantage of this approach is that we could easily add additional scripts to the `application/scripts` directory, without having to repeat the definition of dependencies.

To run the script, we must first create a virtual environment with all dependencies
and then run `main.py` within that environment. First, enter the `application` directory and run

```bash
uv sync
```

This created the `application/.venv` directory. Next run

```bash
uv run scripts/main.py
```
to run the script. You should see a plot of the above function as a result.

You may lock the dependencies by running

```bash
uv lock
```


### 3. Library - `library`

Finally, we move to the library structure, where all reusable code is located in a python package, and the scripts only contain the code that is different for every analysis.

As before, the dependencies are specified in the `pyproject.toml` file and therefore
shared across all scripts as well as with the package. Furthermore, the `main.py` script is located in the `library/scripts` directory. However, this time the `main.py` file imports a module of our own user-defined package, `myproject`, whose source files are located in the `library/src/myproject` directory. The name and the build system of the package are specified in the `pyproject.toml` file.

The main advantage of this structure over the application example stems from the fact that any code within the `myproject` package may now be shared across multiple scripts. This improves code reuse and simplifies maintenance for larger projects.

To run the `main.py` script, we simply follow the same steps as in the previous example: First enter the `library` directory. Run

```bash
uv sync
```

to create the environment and execute the script with

```bash
uv run scripts/main.py
```

You should see the plot of a \[y = x^3\] function. You may lock the dependency versions by running

```bash
uv lock
```

## uv Tipps

The project uses a `src/` layout, which is the default for `uv` projects.

All reusable logic is inside `src/myproject/` and can be imported like.

```python
from myproject import cubic_util
```

Python version is pinned using the .python-version file. This ensures consistent Python versions across collaborators.

Dependencies are declared in `pyproject.toml` and locked in `uv.lock`. You can add a dependency like:
```bash
uv add numpy
```

All code can be run via uv run, which handles virtual environments automatically. Hence, there is no need for manually activating or deactivating environments:
```bash
uv run main.py
```

You can lock your script's dependencies for reproducibility:
```bash
uv lock --script main.py
```

For many more [`uv`](https://github.com/astral-sh/uv) tipps and tricks we refer to the official documentation.