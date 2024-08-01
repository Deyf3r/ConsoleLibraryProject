import os

# Deivi Cristopher Aquino Pérez, 2022 - 2021.

# Lista para almacenar los libros
libros = []

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_encabezado(titulo):
    limpiar_pantalla()
    print("=" * 50)
    print(f"{titulo:^50}")
    print("=" * 50)

def agregar_libro():
    mostrar_encabezado("AGREGAR NUEVO LIBRO")
    codigo = input("Ingrese el código del libro: ")
    titulo = input("Ingrese el título del libro: ")
    apellido_autor = input("Ingrese el apellido del autor: ")
    nombre_autor = input("Ingrese el nombre del autor: ")
    area_conocimiento = input("Ingrese el área de conocimiento: ")
    publicador = input("Ingrese el publicador: ")
    tramo_asignado = input("Ingrese el tramo asignado: ")
    estado = "en sala"  # Por defecto, el libro está en sala

    libro = {
        "codigo": codigo,
        "titulo": titulo,
        "apellido_autor": apellido_autor,
        "nombre_autor": nombre_autor,
        "area_conocimiento": area_conocimiento,
        "publicador": publicador,
        "tramo_asignado": tramo_asignado,
        "estado": estado
    }

    libros.append(libro)
    print("\n" + "-" * 50)
    print("✅ Libro agregado exitosamente.")
    input("\nPresione Enter para continuar...")

def modificar_libro():
    mostrar_encabezado("MODIFICAR LIBRO")
    codigo = input("Ingrese el código del libro a modificar: ")
    for libro in libros:
        if libro["codigo"] == codigo:
            print("\nModificando libro:")
            libro["titulo"] = input("Nuevo título: ")
            libro["apellido_autor"] = input("Nuevo apellido del autor: ")
            libro["nombre_autor"] = input("Nuevo nombre del autor: ")
            libro["area_conocimiento"] = input("Nueva área de conocimiento: ")
            libro["publicador"] = input("Nuevo publicador: ")
            libro["tramo_asignado"] = input("Nuevo tramo asignado: ")
            print("\n" + "-" * 50)
            print("✅ Libro modificado exitosamente.")
            input("\nPresione Enter para continuar...")
            return
    print("\n" + "-" * 50)
    print("❌ Libro no encontrado.")
    input("\nPresione Enter para continuar...")

def mostrar_libros():
    mostrar_encabezado("LISTADO DE LIBROS")
    if not libros:
        print("📚 No hay libros registrados.")
    else:
        for libro in libros:
            print(f"📕 Código: {libro['codigo']}")
            print(f"   Título: {libro['titulo']}")
            print(f"   Autor: {libro['nombre_autor']} {libro['apellido_autor']}")
            print(f"   Área de conocimiento: {libro['area_conocimiento']}")
            print(f"   Publicador: {libro['publicador']}")
            print(f"   Tramo asignado: {libro['tramo_asignado']}")
            print(f"   Estado: {libro['estado']}")
            print("-" * 50)
    input("\nPresione Enter para continuar...")

def buscar_libro():
    mostrar_encabezado("BUSCAR LIBRO")
    codigo = input("Ingrese el código del libro a buscar: ")
    for libro in libros:
        if libro["codigo"] == codigo:
            print("\nLibro encontrado:")
            print(f"📗 Título: {libro['titulo']}")
            print(f"   Autor: {libro['nombre_autor']} {libro['apellido_autor']}")
            print(f"   Área de conocimiento: {libro['area_conocimiento']}")
            print(f"   Publicador: {libro['publicador']}")
            print(f"   Tramo asignado: {libro['tramo_asignado']}")
            print(f"   Estado: {libro['estado']}")
            input("\nPresione Enter para continuar...")
            return
    print("\n" + "-" * 50)
    print("❌ Libro no encontrado.")
    input("\nPresione Enter para continuar...")

def eliminar_libro():
    mostrar_encabezado("ELIMINAR LIBRO")
    codigo = input("Ingrese el código del libro a eliminar: ")
    for libro in libros:
        if libro["codigo"] == codigo:
            libros.remove(libro)
            print("\n" + "-" * 50)
            print("✅ Libro eliminado exitosamente.")
            input("\nPresione Enter para continuar...")
            return
    print("\n" + "-" * 50)
    print("❌ Libro no encontrado.")
    input("\nPresione Enter para continuar...")

# Menú principal
while True:
    mostrar_encabezado("SISTEMA DE BIBLIOTECA")
    print("1. 📚 Agregar libro")
    print("2. 📝 Modificar libro")
    print("3. 📋 Mostrar libros")
    print("4. 🔍 Buscar libro")
    print("5. ❌ Eliminar libro")
    print("6. 🚪 Salir")
    print("-" * 50)

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        agregar_libro()
    elif opcion == "2":
        modificar_libro()
    elif opcion == "3":
        mostrar_libros()
    elif opcion == "4":
        buscar_libro()
    elif opcion == "5":
        eliminar_libro()
    elif opcion == "6":
        mostrar_encabezado("¡GRACIAS POR USAR EL SISTEMA DE BIBLIOTECA!")
        print("Hasta luego. 👋")
        break
    else:
        print("\n❗ Opción no válida. Por favor, intente de nuevo.")
        input("\nPresione Enter para continuar...")