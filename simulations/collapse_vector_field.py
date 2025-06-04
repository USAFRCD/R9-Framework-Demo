import numpy as np
import matplotlib.pyplot as plt

# Generate symbolic collapse vector field
x, y = np.meshgrid(np.linspace(-5, 5, 20), np.linspace(-5, 5, 20))
u = -x / np.sqrt(x**2 + y**2)
v = -y / np.sqrt(x**2 + y**2)

# Clean singularity center
u[np.isnan(u)] = 0
v[np.isnan(v)] = 0

# Plot field
plt.figure(figsize=(6, 6))
plt.quiver(x, y, u, v, color='black')
plt.scatter(0, 0, color='red', s=100, label='⦵ (Collapse Zero)')
plt.title("Symbolic Collapse Vector Field Toward ⦵")
plt.xlabel("Dimensional Axis X")
plt.ylabel("Dimensional Axis Y")
plt.legend()
plt.grid(True)
plt.axis('equal')
plt.tight_layout()
plt.show()