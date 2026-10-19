def dibujar_patron():
    print("--- 2. Pattern ---")
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
if __name__ == "__main__":
    dibujar_patron()