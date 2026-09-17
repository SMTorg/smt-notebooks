# SMT Advanced Notebooks

These notebooks demonstrate advanced usage of the Surrogate Modeling Toolbox (SMT) for various engineering and scientific applications.

## Installation

To run the notebooks locally, install the required dependencies:

```bash
pip install -r requirements.txt
```

## Running the Notebooks

You can open and run the notebooks interactively using Jupyter, Google Colab, or any Jupyter-compatible environment. Click on the "Open In Colab" badges in each section below to run them directly in Google Colab.

### Batch Mode (Error Checking)

A Python script is provided to execute notebooks in batch mode to verify they run without errors. This is useful for CI/CD or testing purposes.

```bash
python execute_notebooks.py [-d DIRECTORY | -f FILE]
```

See the [Script Usage](#script-usage) section at the end of this document for detailed documentation.

---

## Proper Orthogonal Decomposition and Interpolation

* ### PODI+I application to airfoil design

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/SMTorg/smt-use-cases/blob/master/PODI/SMT_PODI_Airfoil.ipynb)

## Kernel Engineering

* ### Kernel engineering application to aeroelasticity prediction

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/SMTorg/smt-use-cases/blob/master/Kernels/SMT_Kernel_Hale.ipynb)

## Mixed-integer and mixed-hierarchical surrogate models

* ### Specific notebook associated to the SMT 2.0 Journal Paper (submitted) with a focus on mixed integer and mixed hierarchical surrogate models (continuous, discrete, categorical)

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/SMTorg/smt-use-cases/blob/master/MixedInteger/RunTestCases_Paper_SMT_v2.ipynb)

* ### Mixed-Integer Gaussian Process and Bayesian Optimization for Engineering application

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/SMTorg/smt-use-cases/blob/master/MixedInteger/SMT_MixedInteger_Engineering_applications.ipynb)


---

## Script Usage

The `execute_notebooks.py` script provides a batch mode to execute notebooks and verify they run without errors. This is primarily intended for testing and CI/CD purposes.

### Installation

First, install the required dependencies:

```bash
pip install -r requirements.txt
```

### Usage

```bash
python execute_notebooks.py [OPTIONS]
```

### Options

- `-d, --directory DIRECTORY`: Search and execute all notebooks recursively in the specified directory (default: current directory)
- `-f, --file FILE`: Execute a specific notebook file
- `-h, --help`: Show help message

### Examples

**Execute all notebooks in the current directory:**
```bash
python execute_notebooks.py
```

**Execute all notebooks in a specific directory:**
```bash
python execute_notebooks.py -d SBO
python execute_notebooks.py -d MultiFi
```

**Execute a single specific notebook:**
```bash
python execute_notebooks.py -f SMT_Tutorial.ipynb
python execute_notebooks.py -f "SBO/SMT_EGO_noisyGP.ipynb"
```

### Output

The script provides detailed output showing:
- List of notebooks found
- Execution status for each notebook (✓ success / ✗ failed)
- Summary with total, passed, and failed counts
- List of failed notebooks if any

The script exits with code `0` if all notebooks succeed, or `1` if any notebook fails.

### Note

This script is designed for **batch execution only** to check for errors. It is not intended for interactive use or development. For interactive work, please use Jupyter Notebook or Jupyter Lab directly.

