from data.biblioteca import libros, categorias
from utils.operaciones import (
    mostrar_disponibles, 
    buscar_por_paginas, 
    contar_libros, 
    promedio_paginas, 
    agregar_categoria
)

continuar = "s"

while continuar == "s":
    print("=== BIBLIOTECA ===")
    print("1. Ver libros disponibles")
    print("2. Buscar libros cortos (menos de 400 páginas)")
    print("3. Ver estadísticas")
    print("4. Agregar categoría")
    print("5. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        mostrar_disponibles(libros)
        
    elif opcion == "2":
        buscar_por_paginas(libros, 400)
        
    elif opcion == "3":
        total = contar_libros(libros)
        promedio = promedio_paginas(libros)
        print("Estadísticas:")
        print("Total de libros registrados:", total)
        print("Promedio de páginas:", promedio)
        
    elif opcion == "4":
        nueva_cat = input("Escribe el nombre de la nueva categoría: ")
        agregar_categoria(categorias, nueva_cat)
        
    elif opcion == "5":
        print("Saliendo del sistema de biblioteca. ¡Hasta luego!")
        continuar = "n"
        
    else:
        print("Opción no válida. Por favor, selecciona un número del 1 al 5.")