import csv
import random
import xml.etree.ElementTree as ET

def procesar_libros(archivo="books.csv"):
    libros = []
    
    try:
        with open(archivo, "r", encoding="windows-1251") as f:
            reader = csv.reader(f, delimiter=";")
            next(reader)
            for row in reader:
                if len(row) > 3:
                    libros.append(row)
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {archivo}")
        return

    idx_titulo = 1
    idx_autor = 2
    idx_anio = 3
    idx_editorial = 4
    idx_popularidad = 5

    titulos_largos = sum(1 for libro in libros if len(libro[idx_titulo]) > 30)
    print(f"1. Libros con título mayor a 30 caracteres: {titulos_largos}")

    autor_buscado = input("2. Autor a buscar: ").strip().lower()
    anios_permitidos = {"2014", "2016", "2017"}
    
    resultados = [
        libro for libro in libros 
        if autor_buscado in libro[idx_autor].lower() and str(libro[idx_anio]) in anios_permitidos
    ]
    
    print(f"   Resultados encontrados ({', '.join(anios_permitidos)}): {len(resultados)}")
    for b in resultados:
        print(f"   - {b[idx_titulo]} ({b[idx_anio]})")

    if len(libros) >= 20:
        seleccion = random.sample(libros, 20)
        with open("referencias.txt", "w", encoding="utf-8") as f_out:
            for i, libro in enumerate(seleccion, 1):
                f_out.write(f"{i}. {libro[idx_autor]}. {libro[idx_titulo]} - {libro[idx_anio]}\n")
        print("3. Archivo 'referencias.txt' creado con éxito.")

    print("\n--- Tareas adicionales ---")
    
    editoriales = set()
    for libro in libros:
        if len(libro) > idx_editorial:
            editoriales.add(libro[idx_editorial].strip())
    print(f"Total de editoriales únicas: {len(editoriales)}")

    try:
        libros_ordenados = sorted(libros, key=lambda x: int(x[idx_popularidad]) if x[idx_popularidad].isdigit() else 0, reverse=True)
        print("Top 20 libros más populares:")
        for i in range(min(20, len(libros_ordenados))):
            print(f"  {i+1}. {libros_ordenados[i][idx_titulo]} (Puntuación: {libros_ordenados[i][idx_popularidad]})")
    except IndexError:
        pass

def procesar_xml(archivo="currency.xml"):
    print("\n--- Procesamiento XML ---")
    try:
        tree = ET.parse(archivo)
        root = tree.getroot()
        
        print("Monedas con Nominal = 1:")
        encontrado = False
        
        for valute in root.findall('Valute'):
            nominal = valute.find('Nominal')
            nombre = valute.find('Name')
            
            if nominal is not None and nombre is not None:
                if nominal.text.strip() == "1":
                    print(f"- {nombre.text}")
                    encontrado = True
                    
        if not encontrado:
            print("No se encontraron resultados.")
            
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {archivo}")
    except ET.ParseError:
        print(f"Error: Formato inválido en {archivo}")

if __name__ == "__main__":
    procesar_libros()
    procesar_xml()