import csv

def leer_datos_desde_csv(nombre_archivo):
    datos = []
    with open(nombre_archivo, 'r') as archivo_csv:
        lector_csv = csv.DictReader(archivo_csv)
        for fila in lector_csv:
            datos.append(fila)
    return datos
def buscar_por_abreviatura(abreviatura, datos):
    for fila in datos:
        if fila['Abr'] == abreviatura:
            return fila['Nombre']
    return None

def buscar_por_nombre(nombre, datos):
    for fila in datos:
        if fila['Nombre'].lower() == nombre.lower():
            return fila['Abr']
    return None
def mostrar_datos(datos):
    for fila in datos:
        print(f"Nombre: {fila['Nombre']}, Abreviatura: {fila['Abr']}, Simbolo: {fila['Simbolo']},"
              f" Código Genético: {fila['Cod.Genetico']},Masa Molar: {fila['Masa Molar']},"
              f"Van Walls: {fila['Van Walls']},Polaridad: {fila['Polaridad']},Hidrofobica: {fila['Hidrofobica']}")

if __name__== "__main__":
    archivo_csv="amino.csv"
    datos=leer_datos_desde_csv(archivo_csv)
    while True:
        print("Escoja una de las siguientes opciones para operar con el csv:")
        print("1- Mostrar todos los aminoácidos del CSV")
        print("2-Buscar por abreviatura")
        print("3-Buscar por nombre")

        opcion=input("Seleciona una opción del 1 al 10: ")

        if opcion == "1":
            mostrar_datos(datos)
        if opcion=="2":
            abreviatura = input("Ingresa la abreviatura del aminoácido: ")
            nombre_encontrado = buscar_por_abreviatura(abreviatura, datos)
            if nombre_encontrado:
                print(f"Nombre del aminoácido con abreviatura '{abreviatura}': {nombre_encontrado}")
            else:
                print(f"No se encontró ningún aminoácido con la abreviatura '{abreviatura}'.")
        elif opcion == "3":
            nombre = input("Ingresa el nombre del aminoácido: ")
            abreviatura_encontrada = buscar_por_nombre(nombre, datos)
            if abreviatura_encontrada:
                print(f"Abreviatura del aminoácido '{nombre}': {abreviatura_encontrada}")
            else:
                print(f"No se encontró ningún aminoácido con el nombre '{nombre}'.")


