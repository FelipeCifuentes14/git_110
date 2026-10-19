RED_BG = '\033[41m'
WHITE_BG = '\033[47m'
BLUE_BG = '\033[44m'
GREEN_BG = '\033[42m'
YELLOW_BG = '\033[43m'
RESET = '\033[0m'

def analizar_secuencia():
    print("--- 4. Análisis de sequence.txt ---")

    with open("sequence.txt") as archivo:
        numeros = [float(n) for n in archivo.read().split()]

    suma_pares = sum(abs(n) for n in numeros[0::2])
    suma_impares = sum(abs(n) for n in numeros[1::2])
    total = suma_pares + suma_impares

    if total == 0:
        print("No hay datos para analizar.")
        return

    porc_pares = suma_pares / total * 100
    porc_impares = 100 - porc_pares

    print(f"Suma posiciones pares: {porc_pares:.1f}%")
    print(f"Suma posiciones impares: {porc_impares:.1f}%")

    ancho_barra = 40
    bloques_pares = round(porc_pares / 100 * ancho_barra)
    bloques_impares = ancho_barra - bloques_pares

    print("Diagrama (Verde = Pares, Amarillo = Impares):")
    print(GREEN_BG + " " * bloques_pares + YELLOW_BG + " " * bloques_impares + RESET)
    print("\n")
    
    
if __name__ == "__main__":
    analizar_secuencia()
