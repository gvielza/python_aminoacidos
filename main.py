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
        if fila['Abr'].lower() == abreviatura.lower():
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
def buscar_simbolo_o_codigo_genetico(valor, datos):
    for fila in datos:
        if valor.upper() == fila['Simbolo']:
            return f"El código genético correspondiente al símbolo '{valor}' es: {fila['Cod.Genetico']}"
        elif valor.upper() == fila['Cod.Genetico']:
            return f"El símbolo correspondiente al código genético '{valor}' es: {fila['Simbolo']}"
    return "No se encontró ningún resultado para el valor ingresado."
def informacion_aminoacido(valor, datos):
    for fila in datos:
        if valor.lower()== fila['Abr'].lower() or valor.upper() == fila['Simbolo']:
            return f"Información del aminoácido con abreviatura/símbolo '{valor}':\n" + \
                   f"Nombre: {fila['Nombre']}\nAbreviatura: {fila['Abr']}\nSimbolo: {fila['Simbolo']}\n" + \
                   f"Código Genético: {fila['Cod.Genetico']}\nMasa Molar: {fila['Masa Molar']}\n" + \
                   f"Van Walls: {fila['Van Walls']}\nPolaridad: {fila['Polaridad']}\nHidrofobica: {fila['Hidrofobica']}"
    return "No se encontró ningún aminoácido con la abreviatura o símbolo ingresado."
def aminoacidos_por_hidrofobicidad(rango_inicio, rango_fin, datos):
    aminoacidos_en_rango = []
    for fila in datos:
        hidrofobicidad = float(fila['Hidrofobica'])
        if rango_inicio <= hidrofobicidad <= rango_fin:
            aminoacidos_en_rango.append(fila['Nombre'])
    return aminoacidos_en_rango
if __name__== "__main__":
    archivo_csv="amino.csv"
    datos=leer_datos_desde_csv(archivo_csv)
    while True:
        print("Escoja una de las siguientes opciones para operar con el csv:")
        print("1- Mostrar todos los aminoácidos del CSV")
        print("2-Buscar por abreviatura")
        print("3-Buscar por nombre")
        print("4-Buscar símbolo dado un codón (U o T) o viceversa.")
        print("5- Información completa de un aminoácido por abreviatura o símbolo")
        print("6- Buscar aminoácidos por rango de interacción hidrofóbica")

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
        elif opcion == "4":
            valor = input("Ingresa un símbolo o un código genético: ")
            resultado = buscar_simbolo_o_codigo_genetico(valor, datos)
            print(resultado)
        elif opcion == "5":
            valor = input("Ingresa la abreviatura o símbolo del aminoácido: ")
            resultado = informacion_aminoacido(valor, datos)
            print(resultado)
        elif opcion == "6":
            rango_inicio = float(input("Ingresa el valor de inicio del rango de interacción hidrofóbica: "))
            rango_fin = float(input("Ingresa el valor de fin del rango de interacción hidrofóbica: "))
            aminoacidos_en_rango = aminoacidos_por_hidrofobicidad(rango_inicio, rango_fin, datos)
            if aminoacidos_en_rango:
                print(f"Aminoácidos con interacción hidrofóbica entre {rango_inicio} y {rango_fin}:")
                print(", ".join(aminoacidos_en_rango))
            else:
                print(f"No se encontraron aminoácidos con interacción hidrofóbica en el rango especificado.")
        else:
            print("Opción inválida. Por favor, elige una opción del 1 al 4.")



