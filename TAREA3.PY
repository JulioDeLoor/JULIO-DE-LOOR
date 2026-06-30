import random
import time

# ==========================
# INICIO DE SESIÓN
# ==========================

USUARIO = "admin"
CONTRASENA = "1234"

print("====================================")
print("      JUEGO DEL AHORCADO")
print("====================================")

usuario = input("Usuario: ")
clave = input("Contraseña: ")

if usuario != USUARIO or clave != CONTRASENA:
    print("\nAcceso denegado.")
    exit()

print("\nBienvenido", usuario)

# ==========================
# BANCO DE PALABRAS
# ==========================

palabras = {
    "PYTHON": "Lenguaje de programación",
    "SOFTWARE": "Conjunto de programas",
    "PROGRAMACION": "Proceso de crear programas",
    "LENGUAJE": "Forma de comunicación",
    "ESTRUCTURA": "Organización de elementos",
    "INGENIERIA": "Carrera relacionada con tecnología"
}

palabra = random.choice(list(palabras.keys()))
pista = palabras[palabra]

# ==========================
# VARIABLES
# ==========================

oculta = ["_"] * len(palabra)
letras_usadas = []
intentos = 6
pista_usada = False

# ==========================
# DIBUJOS DEL AHORCADO
# ==========================

ahorcado = [

"""
 +---+
 |   |
     |
     |
     |
     |
=========
""",

"""
 +---+
 |   |
 O   |
     |
     |
     |
=========
""",

"""
 +---+
 |   |
 O   |
 |   |
     |
     |
=========
""",

"""
 +---+
 |   |
 O   |
/|   |
     |
     |
=========
""",

"""
 +---+
 |   |
 O   |
/|\\  |
     |
     |
=========
""",

"""
 +---+
 |   |
 O   |
/|\\  |
/    |
     |
=========
""",

"""
 +---+
 |   |
 O   |
/|\\  |
/ \\  |
     |
=========
"""
]

# ==========================
# MENÚ
# ==========================

print("\nSeleccione el modo de juego")
print("1. Usuario juega")
print("2. Simulación automática")

modo = input("Opción: ")

# ======================================================
# MODO USUARIO
# ======================================================

if modo == "1":

    while intentos > 0 and "_" in oculta:

        print(ahorcado[6-intentos])

        print("\nPalabra:", " ".join(oculta))
        print("Intentos restantes:", intentos)
        print("Letras usadas:", letras_usadas)

        print("\n1. Ingresar letra")
        print("2. Usar pista")

        opcion = input("Seleccione: ")

        if opcion == "2":

            if not pista_usada:
                print("\nPISTA:", pista)
                pista_usada = True
            else:
                print("La pista ya fue utilizada.")

            continue

        letra = input("Ingrese una letra: ").upper()

        if len(letra) != 1 or not letra.isalpha():
            print("Ingrese solamente una letra.")
            continue

        if letra in letras_usadas:
            print("Ya utilizó esa letra.")
            continue

        letras_usadas.append(letra)

        if letra in palabra:

            print("¡Correcto!")

            for i in range(len(palabra)):
                if palabra[i] == letra:
                    oculta[i] = letra

        else:

            print("Incorrecto")
            intentos -= 1

    print()

    if "_" not in oculta:

        print("¡¡ FELICIDADES !!")
        print("Ganaste la partida.")
        print("Palabra:", palabra)

    else:

        print(ahorcado[6])

        print("Perdiste.")
        print("La palabra era:", palabra)

# ======================================================
# MODO AUTOMÁTICO
# ======================================================

elif modo == "2":

    print("\nSIMULACIÓN AUTOMÁTICA\n")

    letras = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

    while intentos > 0 and "_" in oculta:

        disponibles = [l for l in letras if l not in letras_usadas]

        letra = random.choice(disponibles)

        letras_usadas.append(letra)

        print(ahorcado[6-intentos])

        print("Palabra:", " ".join(oculta))
        print("Probando letra:", letra)

        time.sleep(1)

        if letra in palabra:

            print("La letra existe.\n")

            for i in range(len(palabra)):
                if palabra[i] == letra:
                    oculta[i] = letra

        else:

            print("La letra no existe.\n")
            intentos -= 1

        print("Intentos restantes:", intentos)
        print("------------------------------------")

        time.sleep(1)

    if "_" not in oculta:

        print("\nEl jugador automático ganó.")
        print("Palabra encontrada:", palabra)

    else:

        print(ahorcado[6])

        print("\nEl jugador automático perdió.")
        print("La palabra era:", palabra)

else:
    print("Opción no válida.")