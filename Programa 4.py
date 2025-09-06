''' Ejercicio 4: Función para Calcular el Factorial '''

def factorial(n):
    if n < 0:
        return "El factorial no está definido para números negativos."
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

print(factorial(5))   # Resultado: 120
print(factorial(0))   # Resultado: 1
print(factorial(-3))  # Resultado: mensaje de error
