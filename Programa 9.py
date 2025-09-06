def segundo_mayor(lista):

    if len(lista) < 2:
        return "La lista debe tener al menos dos elementos."

   
    lista_unica = list(set(lista))

 
    if len(lista_unica) < 2:
        return "⚠️ No hay un segundo número distinto en la lista."

    # Ordenar de mayor a menor
    lista_ordenada = sorted(lista_unica, reverse=True)

    # Mostrar resultados
    return (
        f"Lista original: {lista}\n"
        f"Sin duplicados: {lista_unica}\n"
        f"Ordenada: {lista_ordenada}\n"
        f"Segundo mayor: {lista_ordenada[1]}"
    )

# Ejemplos de uso:
print(segundo_mayor([4, 7, 2, 9, 5]))       # Resultado: 7
print(segundo_mayor([10, 10, 10]))          # Resultado: advertencia
print(segundo_mayor([3]))                   # Resultado: advertencia
