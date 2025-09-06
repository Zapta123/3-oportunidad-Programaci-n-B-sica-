''' Ejercicio 2: Número Arbitrario de Argumentos '''

def sumar_todos(*numeros):
    return sum(numeros)

print(sumar_todos(3, 5, 7))           # Resultado: 15
print(sumar_todos(10, -2, 4, 8, 0))   # Resultado: 20
print(sumar_todos())                  # Resultado: 0
