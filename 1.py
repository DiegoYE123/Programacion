articulos = {"id": 1, "nombre": "Ratón", "precio": 12.5, "stock": 20, "activo": True}
id_actual = 1
salir = False

while not salir:
    print("1. Crear")
    print("2. Listar")
    print("3. Buscar por ID")
    print("4. Actualizar")
    print("5. Eliminar")
    print("6. Alternar activo")
    print("7. Salir")

    opcion = input("Opción: ")

    if opcion == "1":
        nombre = input("Nombre: ")
        precio = float(input("Precio: "))
        stock = int(input("Stock: "))
        articulo = {"id": id_actual, "nombre": nombre, "precio": precio, "stock": stock, "activo": True}
        articulos.append(articulo)
        id_actual += 1
        print("Artículo creado.")

    elif opcion == "2":
        print("\n--- Lista de artículos ---")
        for a in articulos:
            estado = "Activo" if a["activo"] else "Inactivo"
            print(a["id"], a["nombre"], a["precio"], a["stock"], estado)

    elif opcion == "3":
        id_buscar = int(input("ID: "))
        encontrado = None
        for a in articulos:
            if a["id"] == id_buscar:
                encontrado = a
        if encontrado:
            print(encontrado)
        else:
            print("No encontrado.")

    elif opcion == "4":
        id_mod = int(input("ID a actualizar: "))
        for a in articulos:
            if a["id"] == id_mod:
                a["nombre"] = input("Nuevo nombre: ")
                a["precio"] = float(input("Nuevo precio: "))
                a["stock"] = int(input("Nuevo stock: "))
                print("Actualizado.")

    elif opcion == "5":
        id_del = int(input("ID a eliminar: "))
        nueva_lista = []
        for a in articulos:
            if a["id"] != id_del:
                nueva_lista.append(a)
        articulos = nueva_lista
        print("Eliminado (si existía).")

    elif opcion == "6":
        id_alt = int(input("ID a alternar: "))
        for a in articulos:
            if a["id"] == id_alt:
                a["activo"] = not a["activo"]
                print("Cambiado estado.")

    elif opcion == "7":
        salir = True
        print("Adiós.")

    else:
        print("Opción no válida.")
