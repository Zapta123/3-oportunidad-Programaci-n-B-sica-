''' Ejercicio 7: Función para Calcular la Mediana '''

def calcular_mediana(lista):
    if not lista:
        return "La lista está vacía. No se puede calcular la mediana."

    lista.sort() 
    n = len(lista)
    mitad = n // 2

    if n % 2 == 0:
        
        mediana = (lista[mitad - 1] + lista[mitad]) / 2
    else:
       
        mediana = lista[mitad]

    return f"Lista ordenada: {lista}\n Mediana: {mediana}"

print(calcular_mediana([7, 3, 9, 1, 5]))       # Impar → Mediana: 5
print(calcular_mediana([10, 2, 8, 4]))         # Par → Mediana: 6.0
print(calcular_mediana([]))                   # Vacía → Mensaje de advertencia
