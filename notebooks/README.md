# SMT Notebooks

These tutorials introduce to use the opensource Surrogate Modeling Toolbox where different surrogate models are available.

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

## SMT Tutorial (linear, quadratic, gaussian process, ...)

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/SMTorg/smt-notebooks/blob/master/SMT_Tutorial.ipynb)


## Surrogate-based Optimization

* ### Efficient Global Optimization: How to start?

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/SMTorg/smt-notebooks/blob/master/SBO/SMT_SBO_EGO_Educational.ipynb)

* ### Bayesian Optimization - Efficient Global Optimization to solve expensive problems

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/SMTorg/smt-notebooks/blob/master/SBO/SMT_EGO_application.ipynb)

* ### Bayesian Optimization with noisy data

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/SMTorg/smt-notebooks/blob/master/SBO/SMT_EGO_noisyGP.ipynb)

## Multi-Fidelity Gaussian Process

* ### With required nested sampling

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/SMTorg/smt-notebooks/blob/master/MultiFi/SMT_MFK_tutorial.ipynb)

* #### With noise

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/SMTorg/smt-notebooks/blob/master/MultiFi/SMT_MFK_Noise.ipynb)

* #### Adaptative sampling

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/SMTorg/smt-notebooks/blob/master/MultiFi/ADOE_MFK_Forrester_1D2F.ipynb)

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/SMTorg/smt-notebooks/blob/master/MultiFi/ADOE_MFK_Rosenbrock_2D2F.ipynb)

* ### Without nested sampling

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/SMTorg/smt-notebooks/blob/master/MultiFi/SMT_MFCK_tutorial.ipynb)

* ### Sparse Multi-fidelity gaussian processes with nested DOE (large database) based on MFK
  
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/SMTorg/smt-notebooks/blob/master/MultiFi/SMT_SMFK_tutorial.ipynb)

* ### Sparse Multi-fidelity gaussian processes with non nested DOE (large database) based on MFCK
  
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/SMTorg/smt-notebooks/blob/master/MultiFi/SMT_SMFCK_tutorial.ipynb)



## Proper Orthogonal Decomposition and Interpolation

* ### PODI+I tutorial in SMT with global and local basis

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/SMTorg/smt-notebooks/blob/master/PODI/SMT_PODI_tutorial.ipynb)

* ### PODI+I application to airfoil design

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/SMTorg/smt-notebooks/blob/master/PODI/SMT_PODI_Airfoil.ipynb)


## Kernel Engineering

* ### Kernel engineering tutorial in SMT

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/SMTorg/smt-notebooks/blob/master/Kernels/SMT_Kernel_tutorial.ipynb)

* ### Kernel engineering application to aeroelasticity prediction

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/SMTorg/smt-notebooks/blob/master/Kernels/SMT_Kernel_Hale.ipynb)

## Explainability and conformal prediction

* ### Warning: [The explainability usage tutorial has been moved to SMTorg/smt-explainability](https://github.com/SMTorg/smt-explainability)

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/SMTorg/smt-explainability/blob/master/tutorial/Explainability_tools.ipynb)


## Other Gaussian Process Models and Sampling Methods

* ### LHS sampling (initial and expanded)

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/SMTorg/smt-notebooks/blob/master/Misc/SMT_ExpandedLHS.ipynb)

* ### Gaussian Process Trajectory Sampling

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/SMTorg/smt-notebooks/blob/master/Misc/SMT_GP_Sampling.ipynb)

* ### Noisy Gaussian Process

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/SMTorg/smt-notebooks/blob/master/Misc/SMT_Noise.ipynb)

* ### Sparse Gaussian Process

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/SMTorg/smt-notebooks/blob/master/Misc/SMT_SGP_analytic.ipynb)


* ### Cooperative Components Kriging

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/SMTorg/smt-notebooks/blob/master/Misc/SMT_CoopCompKRG.ipynb)


## Mixed-integer and mixed-hierarchical surrogate models

* ### Warning: [The Design Space usage tutorial has been moved to SMTorg/smt-design-space-ext](https://github.com/SMTorg/smt-design-space-ext)

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/SMTorg/smt-design-space-ext/blob/master/tutorial/SMT_DesignSpace_example.ipynb)

* ### Specific notebook associated to the SMT 2.0 Journal Paper (submitted) with a focus on mixed integer and mixed hierarchical surrogate models (continuous, discrete, categorical)

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/SMTorg/smt-notebooks/blob/master/MixedInteger/RunTestCases_Paper_SMT_v2.ipynb)

* ### Mixed-Integer Gaussian Process and Bayesian Optimization to solve unconstrained problems with mixed variables (continuous, discrete, categorical)

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/SMTorg/smt-notebooks/blob/master/MixedInteger/SMT_MixedInteger.ipynb)

* ### Mixed-Integer Gaussian Process and Bayesian Optimization for Engineering application

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/SMTorg/smt-notebooks/blob/master/MixedInteger/SMT_MixedInteger_Engineering_applications.ipynb)


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

