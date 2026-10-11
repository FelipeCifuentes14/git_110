import os
import time

if os.name == 'nt':
    os.system('')

RED_BG = '\033[41m'
WHITE_BG = '\033[47m'
BLUE_BG = '\033[44m'
GREEN_BG = '\033[42m'
YELLOW_BG = '\033[43m'
RESET = '\033[0m'

def dibujar_bandera():
    print("--- 1. Bandera de Países Bajos ---")
    ancho = 30
    for _ in range(2):
        print(RED_BG + " " * ancho + RESET)
    for _ in range(2):
        print(WHITE_BG + " " * ancho + RESET)
    for _ in range(2):
        print(BLUE_BG + " " * ancho + RESET)
    print("\n")

def dibujar_patron():
    print("--- 2. Patrón ---")
    ancho = 40
    alto = 5
    
    for i in range(alto):
        linea = ""
        for j in range(ancho):
            if i == 2 and j % 6 == 2:
                linea += "X"
            elif j % 6 == i:
                linea += "\\"
            elif j % 6 == 4 - i:
                linea += "/"
            else:
                linea += " "
        print(linea)
    print("\n")

def analizar_secuencia():
    print("--- 4. Análisis de sequence.txt ---")
    numeros = []
    
    try:
        with open("sequence.txt", "r") as archivo:
            for linea in archivo:
                for num in linea.split(): 
                    numeros.append(float(num))
    except FileNotFoundError:
        print("Archivo no encontrado. Usando datos de prueba...")
        numeros = [10.5, -5.0, 20.1, -15.2, 8.0, 10.0]

    if not numeros:
        return

    suma_pares = 0
    suma_impares = 0

    for i in range(len(numeros)):
        if i % 2 == 0:
            suma_pares += abs(numeros[i])
        else:
            suma_impares += abs(numeros[i])

    total = suma_pares + suma_impares
    
    if total > 0:
        porcentaje_pares = (suma_pares / total) * 100
        porcentaje_impares = (suma_impares / total) * 100

        print(f"Suma posiciones pares: {porcentaje_pares:.1f}%")
        print(f"Suma posiciones impares: {porcentaje_impares:.1f}%")

        ancho_barra = 40
        bloques_pares = int((porcentaje_pares / 100) * ancho_barra)
        bloques_impares = ancho_barra - bloques_pares

        print("Diagrama (Verde = Pares, Amarillo = Impares):")
        print(GREEN_BG + " " * bloques_pares + YELLOW_BG + " " * bloques_impares + RESET)
    print("\n")

def dibujar_grafico():
    print("--- Tarea Extra: Gráfico y = 2x ---")
    alto = 9 
    ancho = 10
    
    for y in range(alto - 1, -1, -1):
        linea = f"{y} |" 
        for x in range(ancho):
            if y == 2 * x:
                linea += " * "
            else:
                linea += "   "
        print(linea)
    
    print("  +" + "-" * (ancho * 3))
    eje_x = "   "
    for x in range(ancho):
        eje_x += f" {x} "
    print(eje_x)
    print("\n")

def animacion():
    print("--- 3. Animación ---")
    input("Presiona ENTER para iniciar...")
    
    frames = [
        "   (•_•)   \n   <)   )╯ \n    /  \\   ",
        "   ( •_•)  \n   \\(   (> \n    /  \\   ",
        "   (•_•)   \n   <)   )╯ \n    /  \\   ",
        "   ( •_•)  \n   \\(   (> \n    /  \\   "
    ]
    
    for _ in range(3):
        for frame in frames:
            comando = "cls" if os.name == "nt" else "clear"
            os.system(comando)
            print("\n" * 5)
            print(frame)
            time.sleep(0.4) 

if __name__ == "__main__":
    dibujar_bandera()
    dibujar_patron()
    analizar_secuencia()
    dibujar_grafico()
    animacion()