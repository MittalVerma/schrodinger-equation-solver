import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import eigh

# Physical constants (set to 1)

hbar = 1.0
m = 1.0

# Spatial grid

L = 1.0           # Length of the box
N = 1000          # Number of grid points
x = np.linspace(0, L, N)
dx = x[1] - x[0]

# Potential (Particle in a Box)

V = np.zeros(N)

# Kinetic energy operator

diag = np.ones(N)
off_diag = -0.5 * np.ones(N-1)

T = (-hbar**2 / (2*m*dx**2)) * (
    np.diag(-2*diag) +
    np.diag(diag[:-1], 1) +
    np.diag(diag[:-1], -1)
)

# Potential energy operator

V_matrix = np.diag(V)

# Hamiltonian

H = T + V_matrix

# Solve eigenvalue problem

energies, wavefunctions = eigh(H)

# Normalize wavefunctions

for i in range(3):
    wavefunctions[:, i] /= np.sqrt(np.trapz(wavefunctions[:, i]**2, x))

# Analytical energies

n = np.array([1, 2, 3])
E_analytical = (n**2 * np.pi**2) / (2 * L**2)

# Print energies

print("Numerical Energies:")
for i in range(3):
    print(f"E{i+1} = {energies[i]:.4f}")

print("\nAnalytical Energies:")
for i in range(3):
    print(f"E{i+1} = {E_analytical[i]:.4f}")

# Plot wavefunctions

plt.figure()
for i in range(3):
    plt.plot(x, wavefunctions[:, i] + energies[i], label=f'n={i+1}')

plt.xlabel("x")
plt.ylabel("Energy + ψ(x)")
plt.title("Particle in a Box: Eigenstates")
plt.legend()
plt.show()
