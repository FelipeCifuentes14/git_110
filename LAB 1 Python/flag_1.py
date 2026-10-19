RED_BG = '\033[41m'
WHITE_BG = '\033[47m'
BLUE_BG = '\033[44m'
GREEN_BG = '\033[42m'
YELLOW_BG = '\033[43m'
RESET = '\033[0m'

def dibujar_bandera():
    print("--- 1. Flag Netherlands ---\n")
    ancho = 30
    for _ in range(2):
        print(RED_BG + " " * ancho + RESET)
    for _ in range(2):
        print(WHITE_BG + " " * ancho + RESET)
    for _ in range(2):
        print(BLUE_BG + " " * ancho + RESET)
    print("\n")

if __name__ == "__main__":
    dibujar_bandera()