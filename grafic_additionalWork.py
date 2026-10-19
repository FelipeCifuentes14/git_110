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
    
if __name__ == "__main__":
    dibujar_grafico()
       
    