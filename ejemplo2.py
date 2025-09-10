import numpy as np
import matplotlib.pyplot as plt

# Parámetros de la esfera
u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, np.pi, 100)
U, V = np.meshgrid(u, v)

# Fórmulas paramétricas
x = np.cos(U) * np.sin(V)
y = np.sin(U) * np.sin(V)
z = np.cos(V)

# Graficar
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z, color='blue', alpha=0.7)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Esfera 3D: $x^2 + y^2 + z^2 = 1$')
plt.show()# Guardar la figura