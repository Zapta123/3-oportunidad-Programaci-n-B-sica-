''' Ejercicio 5: Función para Calcular el Promedio '''

def calcular_promedio(calificaciones):
    # Verificar si la lista está vacía
    if not calificaciones:
        return "La lista está vacía. No se puede calcular el promedio."

    # Calcular suma total y cantidad de elementos
    suma = sum(calificaciones)
    cantidad = len(calificaciones)
    promedio = suma / cantidad

    mensaje = (
        f"📊 Calificaciones: {calificaciones}\n"
        f"🔢 Suma total: {suma}\n"
        f"📈 Número de elementos: {cantidad}\n"
        f"✅ Promedio: {round(promedio, 2)}"
    )
    return mensaje

print(calcular_promedio([85, 90, 78, 92]))
