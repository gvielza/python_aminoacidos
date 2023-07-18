import csv


def leer_datos_csv(nombre_archivo):
    datos=[]
    with open(nombre_archivo,'r') as archivo_csv:
        lector_csv=csv.reader(archivo_csv)
        for fila in lector_csv:
            datos.append(fila)
    return datos


def mostrar_datos(datos):
    for fila in datos:
        print(datos)



if __name__== "__main__":
    archivo_csv="amino.csv"
    datos=leer_datos_csv(archivo_csv)
    while True:
        print("Escoja una de las siguientes opciones para operar con el csv:")
        print("1- Mostrar todos los aminoácidos del CSV")

        opcion=input("Seleciona una opción del 1 al 10: ")

        if opcion == "1":
            mostrar_datos(datos)


