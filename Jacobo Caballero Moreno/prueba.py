import json

# Diccionario donde se almacena estudiantes
estudiantes = {}


#datos en JSON

def guardar_datos():
    with open("estudiantes.json", "w") as archivo:
        json.dump(estudiantes, archivo, indent=4)

def cargar_datos():
    global estudiantes
    try:
        with open("estudiantes.json", "r") as archivo:
            estudiantes = json.load(archivo)
    except FileNotFoundError:
        estudiantes = {}

def agregar_estudiante():
    cedula = input("Ingrese la cédula del estudiante: ")
    if cedula in estudiantes:
        print("El estudiante ya está registrado.")
        return
    nombre = input("Ingrese el nombre del estudiante: ")
    apellido = input("Ingrese el apellido del estudiante: ")
    edad = int(input("Ingrese la edad del estudiante: "))
    estudiantes[cedula] = {"nombre": nombre, "apellido": apellido, "edad": edad, "materias": {}}
    print("Estudiante agregado correctamente.")
    guardar_datos()

def agregar_materia():
    cedula = input("Ingrese la cédula del estudiante: ")
    if cedula not in estudiantes:
        print("El estudiante no está registrado.")
        return
    materia = input("Ingrese el nombre de la materia: ")
    if materia in estudiantes[cedula]["materias"]:
        print("La materia ya existe para este estudiante.")
    else:
        estudiantes[cedula]["materias"][materia] = []
        print("Materia agregada.")
        guardar_datos()


def agregar_nota():
    cedula = input("Ingrese la cédula del estudiante: ")
    if cedula not in estudiantes:
        print("El estudiante no está registrado.")
        return
    materia = input("Ingrese la materia a la que desea agregar nota: ")
    if materia not in estudiantes[cedula]["materias"]:
        print("La materia no existe para este estudiante.")
        return
    nota = float(input("Ingrese la nota: "))
    estudiantes[cedula]["materias"][materia].append(nota)
    print("Nota agregada.")
    guardar_datos()

def consultar_promedio_estudiante():
    cedula = input("Ingrese la cédula del estudiante: ")
    if cedula not in estudiantes:
        print("El estudiante no está registrado.")
        return
    
    suma_total = 0
    cantidad_notas = 0
    for notas in estudiantes[cedula]["materias"].values():
        suma_total += sum(notas)
        cantidad_notas += len(notas)
    
    if cantidad_notas == 0:
        print("El estudiante no tiene notas registradas.")
    else:
        promedio = suma_total / cantidad_notas
        print(f"El promedio del estudiante es: {promedio:.2f}")

def promedio_por_materia():
    materia = input("Ingrese el nombre de la materia: ")
    total = 0
    cantidad = 0
    for datos in estudiantes.values():
        if materia in datos["materias"]:
            total += sum(datos["materias"][materia])
            cantidad += len(datos["materias"][materia])
    if cantidad == 0:
        print("No hay notas registradas para esta materia.")
    else:
        print(f"El promedio general en {materia} es: {total / cantidad:.2f}")

def mostrar_aprobados_reprobados():
    print("\n--- Aprobados y Reprobados ---")
    for cedula, datos in estudiantes.items():
        suma = 0
        total_notas = 0
        for notas in datos["materias"].values():
            suma += sum(notas)
            total_notas += len(notas)
        if total_notas > 0:
            promedio = suma / total_notas
            estado = "APROBADO" if promedio >= 6.0 else "REPROBADO"
            print(f"{datos['nombre']} {datos['apellido']} - {estado} (Promedio: {promedio:.2f})")

def estadisticas_generales():
    todas_las_notas = []
    for datos in estudiantes.values():
        for notas in datos["materias"].values():
            todas_las_notas.extend(notas)
    if todas_las_notas:
        print(f"Mayor nota: {max(todas_las_notas)}")
        print(f"Menor nota: {min(todas_las_notas)}")
        print(f"Promedio general: {sum(todas_las_notas)/len(todas_las_notas):.2f}")
    else:
        print("No hay notas registradas.")

def menu():
    cargar_datos()
    while True:
        print("\n--- MENÚ ---")
        print("1. Agregar estudiante")
        print("2. Agregar materia")
        print("3. Agregar nota")
        print("4. Consultar promedio por estudiante")
        print("5. Promedio general por materia")
        print("6. Ver aprobados y reprobados")
        print("7. Estadísticas generales")
        print("8. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_estudiante()
        elif opcion == "2":
            agregar_materia()
        elif opcion == "3":
            agregar_nota()
        elif opcion == "4":
            consultar_promedio_estudiante()
        elif opcion == "5":
            promedio_por_materia()
        elif opcion == "6":
            mostrar_aprobados_reprobados()
        elif opcion == "7":
            estadisticas_generales()
        elif opcion == "8":
            print("Saliendo...")
            break
        else:
            print("Opción inválida, intente de nuevo.")

menu()
