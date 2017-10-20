# NonLinDyn
Code for homework in Nonlinear Dynamics course from Complexity Explorer.
## Contents:
### Euler.py
Implementation of several ODE solvers in the Euler family.
1. Forward (implicit) Euler
2. Backward (explicit) Euler
3. Trapezoid
4. 4th Order Runge-Kutta (unfinished)

ODE systems available:
1. Simple Harmonic Oscillator: v' = -(k/m)x - bv
2. Lorentz Equations: 
    - x' = sigma\*(y - x)
    - y' = x\*(rho - z) - y
    - z' = x\*y - beta\*z
