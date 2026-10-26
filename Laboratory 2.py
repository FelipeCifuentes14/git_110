
import csv
import xml.etree.ElementTree as ET


# Elegir el archivo de libros



# Leer los libros
with open("books-en.csv", "r", encoding ="latin-1", newline = "") as f:
    lector = csv.DictReader(f,delimiter=";")
    libros = list(lector)

# Mostrar las columnas del archivo
print("Columnas:", libros[0].keys())


while True:
    print("\n--- LABORATORIO 2 ---")
    print("1. Contar titulos largos")
    print("2. Buscar libros por autor")
    print("3. Crear referencias bibliograficas")
    print("4. Leer monedas del XML")
    print("5. Mostrar etiquetas sin repetir")
    print("6. Mostrar los 20 libros mas populares")
    print("0. Salir")

    opcion = input("Elige una opcion: ")

    # 1. Contar titulos de mas de 30 caracteres
    if opcion == "1":
        cantidad = 0

        for libro in libros:
            if len(libro["Book-Title"]) > 30:
                cantidad += 1

        print("Cantidad de titulos largos:", cantidad)

    # 2. Buscar libros por autor
    elif opcion == "2":
        autor_buscado = input("Escribe el autor: ").lower()
        encontrados = 0

        for libro in libros:
            autor = libro["Book-Author"].lower()
            anio = libro["Year-Of-Publication"]

            if autor_buscado in autor:
                if anio <= "1990":
                    print(
                        libro["Book-Title"],
                        "-", libro["Book-Author"],
                        "-", anio
                    )
                    encontrados += 1

        if encontrados == 0:
            print("No se encontraron libros con ese autor y esos años.")

    # 3. Crear referencias bibliograficas
    elif opcion == "3":
        with open("referencias.txt", "w", encoding="utf-8") as f:
            numero = 1

            for libro in libros[:20]:
                referencia = (
                    str(numero) + ". "
                    + libro["Book-Author"] + ". "
                    + libro["Book-Title"] + " - "
                    + libro["Year-Of-Publication"]
                )

                f.write(referencia + "\n")
                numero += 1

        print("Se ha creado el archivo referencias.txt")

    # 4. Leer monedas del XML
    elif opcion == "4":
        arbol = ET.parse("currency.xml")
        raiz = arbol.getroot()

        nombres = []

        for moneda in raiz.iter("Valute"):
            nominal = moneda.find("Nominal").text
            nombre = moneda.find("Name").text

            if nominal == "1":
                nombres.append(nombre)

        print("Monedas con nominal igual a 1:")
        print(nombres)

    # 5. Mostrar etiquetas sin repetir
    elif opcion == "5":
        etiquetas = []

        for libro in libros:
            if "Теги" in libro:
                texto = libro["Теги"]

                for etiqueta in texto.split(","):
                    etiqueta = etiqueta.strip()

                    if etiqueta != "" and etiqueta not in etiquetas:
                        etiquetas.append(etiqueta)

        etiquetas.sort()

        for etiqueta in etiquetas:
            print(etiqueta)

    # 6. Mostrar los 20 libros mas populares
    elif opcion == "6":
        frecuencia = {}

        for libro in libros:
            titulo = libro["Book-Title"]

            if titulo in frecuencia:
                frecuencia[titulo] += 1
            else:
                frecuencia[titulo] = 1

        populares = sorted(
            frecuencia,
            key=frecuencia.get,
            reverse=True
        )

        for titulo in populares[:20]:
            print(titulo, "-", frecuencia[titulo], "apariciones")

    # Salir
    elif opcion == "0":
        print("Programa terminado.")
        break

    else:
        print("Opcion incorrecta.")
