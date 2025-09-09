import numpy as np
import matplotlib.pyplot as plt

# Parámetros de la distribución normal
media = 0
desviacion = 1

# Valores del eje x
x = np.linspace(media - 4*desviacion, media + 4*desviacion, 1000)

# Función de densidad de probabilidad (PDF) calculada manualmente
y = (1 / (desviacion * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - media) / desviacion)**2)

plt.plot(x, y, label='Distribución Normal')
plt.title('Campana de Gauss')
plt.xlabel('Valores')
plt.ylabel('Densidad de probabilidad')
plt.legend()
plt.grid(True)
plt.show()