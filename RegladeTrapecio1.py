import numpy as np

# Definimos la función a integrar
def f(x):
    return x**2 + 3*x + 1

# Implementación de la regla del trapecio
def trapezoidal_rule(a, b, n):
    x = np.linspace(a, b, n+1)  # Puntos equidistantes
    y = f(x)
    h = (b - a) / n
    integral = (h / 2) * (y[0] + 2 * sum(y[1:n]) + y[n])  # Regla del trapecio compuesta
    return integral

# Parámetros de integración
a, b = 0, 2  # Intervalo de integración
n_values = [10, 20, 50]  # Número de subdivisiones

# Solución exacta de la integral
def exact_integral():
    return (2**3)/3 + (3*(2**2))/2 + 2

exact_value = exact_integral()

# Calculamos las aproximaciones y los errores
for n in n_values:
    integral_approx = trapezoidal_rule(a, b, n)
    error = abs(exact_value - integral_approx)
    print(f"n = {n}: Integral aproximada = {integral_approx:.6f}, Error = {error:.6f}")

# Imprimimos la solución exacta
print(f"\nSolución exacta: {exact_value:.6f}")
