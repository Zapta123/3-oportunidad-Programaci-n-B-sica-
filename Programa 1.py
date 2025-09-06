''' Ejercicio 1: Función con Valores por Omisión '''

def saludar(nombre, edad=18):
    print(f"Hola {nombre}, tienes {edad} años.")

# Ejemplos de uso:
saludar("Ana")           # No se proporciona edad, se asume 18
saludar("Luis", 25)      # Se proporciona edad
