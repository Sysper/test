def contar_palabras(cadena):
   
    palabras = cadena.split()
    
    return len(palabras)


texto = input("Ingresa una frase para contar cuantas palabras contiene: ")

cantidad_palabras = contar_palabras(texto)

print(f"La frase tiene {cantidad_palabras} palabras.")