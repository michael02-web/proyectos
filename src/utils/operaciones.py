from models.libro import Libro

def promedio_paginas(libros: list[Libro]):
    total_paginas = 0
    for libro in libros:
        total_paginas += libro["paginas"]
    return total_paginas / len(libros)

def contar_libros(libros: list[Libro]):
    return len(libros)

def mostrar_disponibles(lista_libros: list[Libro]):
    print("\n--- Libros Disponibles ---")
    for libro in lista_libros:
        if libro["disponible"] == True: 
            print(f"- {libro['titulo']} (Autor: {libro['autor']})")

def buscar_por_paginas(lista_libros: list[Libro], max_paginas: int):
    print(f"\n--- Libros con menos de {max_paginas} páginas ---")
    for libro in lista_libros:
        if libro["paginas"] < max_paginas:
            print(f"- {libro['titulo']} ({libro['paginas']} páginas)")

def agregar_categoria(set_categorias: set[str], nueva_categoria: str):
    set_categorias.add(nueva_categoria)
    print(f"\nCategoría '{nueva_categoria}' agregada con éxito.")
    print(f"Categorías actuales: {set_categorias}")