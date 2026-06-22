import random

# Banco de palabras
palabras = [
    "python",
    "computadora",
    "programacion",
    "algoritmo",
    "variable",
    "funcion",
    "condicional",
    "bucle",
    "software",
    "desarrollo"
]

# Seleccionar palabra aleatoria
palabra = random.choice(palabras)

# Crear lista de guiones
oculta = ["_"] * len(palabra)

# Numero de intentos
intentos = 6

# Letras utilizadas
letras_usadas = []

print("================================")
print("      JUEGO DEL AHORCADO")
print("================================")

while intentos > 0 and "_" in oculta:

    print("\nPalabra:", " ".join(oculta))
    print("Intentos restantes:", intentos)
    print("Letras usadas:", letras_usadas)

    letra = input("Ingrese una letra: ").lower()

    # Verificar si ya fue utilizada
    if letra in letras_usadas:
        print("Ya utilizaste esa letra.")
        continue

    letras_usadas.append(letra)

    # Verificar si la letra esta en la palabra
    if letra in palabra:

        for i in range(len(palabra)):
            if palabra[i] == letra:
                oculta[i] = letra

        print("Correcto")

    else:
        intentos -= 1
        print("Letra incorrecta.")

# Resultado final
if "_" not in oculta:
    print("\n================================")
    print("FELICIDADES, GANASTE")
    print("La palabra era:", palabra)
    print("================================")
else:
    print("\n================================")
    print("PERDISTE, INTENTA NUEVAMENTE")
    print("La palabra era:", palabra)
    print("================================")