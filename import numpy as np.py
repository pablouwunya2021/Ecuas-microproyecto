import numpy as np
import matplotlib.pyplot as plt

# Constantes
lambda_ = 1.342  # Constante de decaimiento

# Definir la función de decaimiento
def dN_dt(N, t):
    return -lambda_ * N

# Generar una cuadrícula de valores para N y t
N = np.linspace(-20, 20, 40)  # Valores de N, incluyendo negativos
t = np.linspace(-5, 5, 50)   # Valores de t, incluyendo negativos

# Crear una cuadrícula de coordenadas (t, N)
T, N = np.meshgrid(t, N)

# Calcular dN/dt para cada punto en la cuadrícula
dN = dN_dt(N, T)

# Graficar el campo direccional
plt.figure(figsize=(10, 6))
plt.quiver(T, N, np.ones_like(dN), dN, angles='xy')
plt.xlabel('Tiempo (t)')
plt.ylabel('Número de núcleos (N)')
plt.title('Campo direccional de la ecuación de decaimiento radiactivo')
plt.grid()
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.show()

# Graficar el diagrama de fase
N0 = 20  # Condición inicial
t_vals = np.linspace(-5, 5, 200)
N_vals_pos = N0 * np.exp(-lambda_ * t_vals)
N_vals_neg = -N0 * np.exp(-lambda_ * t_vals)

plt.figure(figsize=(10, 6))
plt.plot(t_vals, N_vals_pos, 'r-', label=f'$N(t) = {N0}e^{{-{lambda_:.2f}t}}$')
plt.plot(t_vals, N_vals_neg, 'b--', label=f'$N(t) = -{N0}e^{{-{lambda_:.2f}t}}$')
plt.xlabel('Tiempo (t)')
plt.ylabel('Número de núcleos (N)')
plt.title('Diagrama de fase de la ecuación de decaimiento radiactivo')
plt.legend()
plt.grid()
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.show()


