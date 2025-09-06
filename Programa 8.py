'''Ejercicio 8: Función para Verificar Palíndromo'''

def es_palindromo(texto):
    texto_normalizado = texto.replace(" ", "").lower()
    
    invertido = texto_normalizado[::-1]
    
    if texto_normalizado == invertido:
        return f"'{texto}' es un palíndromo."
    else:
        return f"'{texto}' no es un palíndromo."

print(es_palindromo("Anita lava la tina"))   # Palíndromo
print(es_palindromo("Hola mundo"))           # No palíndromo
print(es_palindromo("Reconocer"))            # Palíndromo
