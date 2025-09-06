def calcular_mcd(a, b):

    a, b = abs(a), abs(b)

    while b != 0:
        a, b = b, a % b

    return f"El MCD es: {a}"

# Ejemplos de uso:
print(calcular_mcd(48, 18))     # Resultado: 6
print(calcular_mcd(100, 25))    # Resultado: 25
print(calcular_mcd(-36, 60))    # Resultado: 12
