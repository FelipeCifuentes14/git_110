
# Bandera de Colombia

#ESC[0m Eliminar color de todo, necesario par empezar / reiniciar formato
#"\x1b[" = ESC  ESC es para: (en este momento se van a usar los codigos)

o = "\x1b[" 
RESET = f"{o}0m" #codigo de RESET

YELLOW = 220
BLUE = 27
RED = 196
franjas = [YELLOW, BLUE, RED]

def color(borrar, colorear): #ESC[48;5;{ID}m	Set background color. para llamar cod. ANSI y pintar el color del fondo
    return f"{o}48;5;{colorear}m{borrar}{RESET}"  # se cierra siempre con "m" 

ancho = 40
largo = 10

def pintar():
    for i in range(largo):
        
        colorear = franjas[i * len(franjas)//largo]  #/ division con decimales //division entero
        print(color(" " * ancho, colorear))

if __name__ == "__main__":
    pintar()

