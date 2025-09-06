'''Ejercicio 12: Cálculo de la Moda'''

def calcular_moda(lista):
    if not lista:
        return "La lista está vacía."
    
    conteo = {}
    for numero in lista:
        if numero in conteo:
            conteo[numero] += 1
        else:
            conteo[numero] = 1

    
    moda = max(conteo, key=conteo.get)
    frecuencia = conteo[moda]

    return f"La moda es {moda}, aparece {frecuencia} veces."

# Ejemplo de uso:
print(calcular_moda([4, 2, 4, 3, 2, 4]))
