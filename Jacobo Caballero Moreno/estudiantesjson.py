import json
import os


ESTUDIANTES_JSON_PATH = r"C:\Users\jacko\Documents\Programación\Trabajos Lenguaje\estudiantes.json"


estudiantes = {}

def cargar_estudiantes():
    global estudiantes
    if os.path.exists(ESTUDIANTES_JSON_PATH):
        with open(ESTUDIANTES_JSON_PATH, "r", encoding="utf-8") as f:
            estudiantes = json.load(f)
    else:
        estudiantes = {}

def guardar_estudiantes():
    with open(ESTUDIANTES_JSON_PATH, "w", encoding="utf-8") as f:
        json.dump(estudiantes, f, indent=4, ensure_ascii=False)

def agregar_estudiante():
    cedula = input("Ingrese la cédula del estudiante: ").strip()
    if cedula in estudiantes:
        print("Ya existe.")
        return
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    edad = input("Edad: ")
    estudiantes[cedula] = {"nombre": nombre, "apellido": apellido, "edad": edad, "materias": {}}
    guardar_estudiantes()
    print("Estudiante agregado.")

def agregar_materia():
    cedula = input("Cédula del estudiante: ").strip()
    if cedula not in estudiantes:
        print("No encontrado.")
        return
    materia = input("Materia: ")
    if materia in estudiantes[cedula]["materias"]:
        print("Materia ya existe.")
    else:
        estudiantes[cedula]["materias"][materia] = []
        guardar_estudiantes()
        print("Materia agregada.")

def agregar_nota():
    cedula = input("Cédula: ").strip()
    if cedula not in estudiantes:
        print("No encontrado.")
        return
    materia = input("Materia: ")
    if materia not in estudiantes[cedula]["materias"]:
        print("Materia no existe.")
        return
    nota = float(input("Nota: "))
    estudiantes[cedula]["materias"][materia].append(nota)
    guardar_estudiantes()
    print("Nota agregada.")

def consultar_promedio():
    cedula = input("Cédula: ").strip()
    if cedula not in estudiantes:
        print("No encontrado.")
        return
    materias = estudiantes[cedula]["materias"]
    if not materias:
        print("No tiene materias.")
        return
    suma, cantidad = 0, 0
    for notas in materias.values():
        suma += sum(notas)
        cantidad += len(notas)
    if cantidad == 0:
        print("No tiene notas.")
    else:
        print(f"Promedio: {suma / cantidad:.2f}")

def menu():
    cargar_estudiantes()
    while True:
        print("\n1. Agregar estudiante")
        print("2. Agregar materia")
        print("3. Agregar nota")
        print("4. Consultar promedio")
        print("5. Salir")
        opcion = input("Opción: ")

        if opcion == "1":
            agregar_estudiante()
        elif opcion == "2":
            agregar_materia()
        elif opcion == "3":
            agregar_nota()
        elif opcion == "4":
            consultar_promedio()
        elif opcion == "5":
            print("Saliendo...")
            break
        else:
            print("Opción inválida.")

menu()
