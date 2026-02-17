# schrodinger-equation-solver
Numerical solution of Schrödinger equation using finite difference method in Python
Numerical Solution of Schrödinger Equation

This project implements a numerical solution of the time-independent Schrödinger equation for a particle in a one-dimensional box using finite difference methods.

#Overview

The Schrödinger equation is solved by discretizing space and constructing the Hamiltonian matrix consisting of kinetic and potential energy operators. The eigenvalue problem is then solved numerically to obtain energy eigenvalues and corresponding wavefunctions.

#Method

Finite difference approximation for second derivative

Hamiltonian matrix construction

Eigenvalue solution using SciPy linear algebra tools

Normalization of eigenfunctions

Comparison with analytical energy values

#Technologies Used

Python

NumPy

SciPy

Matplotlib

#Results

The numerical energy eigenvalues closely match analytical solutions for the particle-in-a-box system. The first three eigenstates and corresponding wavefunctions are visualized.

## Detailed Explanation

A detailed mathematical explanation and derivation can be found here:

[Project Report (PDF)](report.pdf)
