#Entrega 1

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
        
# Entrega 2

usuarios = []
siguiente_id = 1
opcion = 0

while opcion != 7:
    print()
    print("=== MENÚ USUARIOS ===")
    print("1. Crear usuario")
    print("2. Listar usuarios")
    print("3. Buscar usuario por id")
    print("4. Actualizar usuario")
    print("5. Eliminar usuario")
    print("6. Activar/Inactivar usuario")
    print("7. Salir")

    opcion = int(input("Elige una opción: "))

    if opcion == 1:
        print()
        print("--- Crear usuario ---")
        nombre = input("Nombre: ")
        email = input("Email: ")

        if "@" in email and "." in email:
            usuario = {"id": siguiente_id, "nombre": nombre, "email": email, "activo": True}
            usuarios.append(usuario)
            print("Usuario creado con id", siguiente_id)
            siguiente_id = siguiente_id + 1
        else:
            print("Email inválido")

    if opcion == 2:
        print()
        print("--- Lista de usuarios ---")
        if len(usuarios) == 0:
            print("No hay usuarios.")
        else:
            i = 0
            while i < len(usuarios):
                u = usuarios[i]
                estado = "Activo"
                if u["activo"] == False:
                    estado = "Inactivo"
                print(u["id"], "-", u["nombre"], "-", u["email"], "-", estado)
                i = i + 1

    if opcion == 3:
        print()
        print("--- Buscar usuario por id ---")
        id_buscar = int(input("Id: "))
        i = 0
        encontrado = None
        while i < len(usuarios):
            if usuarios[i]["id"] == id_buscar:
                encontrado = usuarios[i]
            i = i + 1
        if encontrado == None:
            print("No encontrado")
        else:
            print("Usuario:", encontrado["id"], "-", encontrado["nombre"], "-", encontrado["email"])

    if opcion == 4:
        print()
        print("--- Actualizar usuario ---")
        id_actualizar = int(input("Id: "))
        i = 0
        usuario = None
        while i < len(usuarios):
            if usuarios[i]["id"] == id_actualizar:
                usuario = usuarios[i]
            i = i + 1
        if usuario == None:
            print("No encontrado")
        else:
            nuevo_nombre = input("Nuevo nombre (vacío para no cambiar): ")
            nuevo_email = input("Nuevo email (vacío para no cambiar): ")

            if nuevo_nombre != "":
                usuario["nombre"] = nuevo_nombre
            if nuevo_email != "":
                if "@" in nuevo_email and "." in nuevo_email:
                    usuario["email"] = nuevo_email
                else:
                    print("Email no válido, no se cambió")
            print("Usuario actualizado")

    if opcion == 5:
        print()
        print("--- Eliminar usuario ---")
        id_eliminar = int(input("Id: "))
        i = 0
        pos = -1
        while i < len(usuarios):
            if usuarios[i]["id"] == id_eliminar:
                pos = i
            i = i + 1
        if pos == -1:
            print("No encontrado")
        else:
            del usuarios[pos]
            print("Usuario eliminado")

    if opcion == 6:
        print()
        print("--- Activar / Inactivar usuario ---")
        id_cambiar = int(input("Id: "))
        i = 0
        usuario = None
        while i < len(usuarios):
            if usuarios[i]["id"] == id_cambiar:
                usuario = usuarios[i]
            i = i + 1
        if usuario == None:
            print("No encontrado")
        else:
            if usuario["activo"] == True:
                usuario["activo"] = False
                print("Usuario ahora inactivo")
            else:
                usuario["activo"] = True
                print("Usuario ahora activo")

print()
print("Programa terminado.")

# Entrega 3

articulos = []
usuarios = []
ventas = []
carrito = []
usuario_activo = None

id_art = 1
id_usr = 1
id_venta = 1

opcion = 0

while opcion != 4:
    print()
    print("=== MENÚ PRINCIPAL ===")
    print("1. Usuarios")
    print("2. Artículos")
    print("3. Ventas / Carrito")
    print("4. Salir")
    opcion = int(input("Elige una opción: "))

   
    if opcion == 1:
        op_u = 0
        while op_u != 7:
            print()
            print("--- MENÚ USUARIOS ---")
            print("1. Crear usuario")
            print("2. Listar usuarios")
            print("3. Buscar usuario")
            print("4. Actualizar usuario")
            print("5. Eliminar usuario")
            print("6. Activar/Inactivar")
            print("7. Volver")
            op_u = int(input("Opción: "))

            if op_u == 1:
                nombre = input("Nombre: ")
                email = input("Email: ")
                if "@" in email and "." in email:
                    usuario = {"id": id_usr, "nombre": nombre, "email": email, "activo": True}
                    usuarios.append(usuario)
                    print("Usuario creado con id", id_usr)
                    id_usr = id_usr + 1
                else:
                    print("Email inválido")

            if op_u == 2:
                if len(usuarios) == 0:
                    print("No hay usuarios.")
                else:
                    i = 0
                    while i < len(usuarios):
                        u = usuarios[i]
                        est = "Activo"
                        if u["activo"] == False:
                            est = "Inactivo"
                        print(u["id"], "-", u["nombre"], "-", u["email"], "-", est)
                        i = i + 1

            if op_u == 3:
                id_b = int(input("ID: "))
                i = 0
                enc = None
                while i < len(usuarios):
                    if usuarios[i]["id"] == id_b:
                        enc = usuarios[i]
                    i = i + 1
                if enc == None:
                    print("No encontrado")
                else:
                    print(enc)

            if op_u == 4:
                id_a = int(input("ID: "))
                i = 0
                usr = None
                while i < len(usuarios):
                    if usuarios[i]["id"] == id_a:
                        usr = usuarios[i]
                    i = i + 1
                if usr == None:
                    print("No encontrado")
                else:
                    nuevo = input("Nuevo nombre: ")
                    nuevoe = input("Nuevo email: ")
                    if nuevo != "":
                        usr["nombre"] = nuevo
                    if nuevoe != "":
                        if "@" in nuevoe and "." in nuevoe:
                            usr["email"] = nuevoe
                        else:
                            print("Email inválido")

            if op_u == 5:
                id_e = int(input("ID: "))
                i = 0
                pos = -1
                while i < len(usuarios):
                    if usuarios[i]["id"] == id_e:
                        pos = i
                    i = i + 1
                if pos == -1:
                    print("No encontrado")
                else:
                    del usuarios[pos]
                    print("Eliminado")

            if op_u == 6:
                id_c = int(input("ID: "))
                i = 0
                usr = None
                while i < len(usuarios):
                    if usuarios[i]["id"] == id_c:
                        usr = usuarios[i]
                    i = i + 1
                if usr == None:
                    print("No encontrado")
                else:
                    if usr["activo"]:
                        usr["activo"] = False
                        print("Usuario inactivo")
                    else:
                        usr["activo"] = True
                        print("Usuario activo")

 
    if opcion == 2:
        op_a = 0
        while op_a != 6:
            print()
            print("--- MENÚ ARTÍCULOS ---")
            print("1. Crear artículo")
            print("2. Listar artículos")
            print("3. Buscar artículo")
            print("4. Actualizar artículo")
            print("5. Eliminar artículo")
            print("6. Volver")
            op_a = int(input("Opción: "))

            if op_a == 1:
                nombre = input("Nombre: ")
                precio = float(input("Precio: "))
                stock = int(input("Stock: "))
                art = {"id": id_art, "nombre": nombre, "precio": precio, "stock": stock, "activo": True}
                articulos.append(art)
                print("Artículo creado con id", id_art)
                id_art = id_art + 1

            if op_a == 2:
                if len(articulos) == 0:
                    print("No hay artículos.")
                else:
                    i = 0
                    while i < len(articulos):
                        a = articulos[i]
                        est = "Activo"
                        if a["activo"] == False:
                            est = "Inactivo"
                        print(a["id"], "-", a["nombre"], "-", a["precio"], "-", a["stock"], "-", est)
                        i = i + 1

            if op_a == 3:
                id_b = int(input("ID: "))
                i = 0
                enc = None
                while i < len(articulos):
                    if articulos[i]["id"] == id_b:
                        enc = articulos[i]
                    i = i + 1
                if enc == None:
                    print("No encontrado")
                else:
                    print(enc)

            if op_a == 4:
                id_a2 = int(input("ID: "))
                i = 0
                art = None
                while i < len(articulos):
                    if articulos[i]["id"] == id_a2:
                        art = articulos[i]
                    i = i + 1
                if art == None:
                    print("No encontrado")
                else:
                    nuevo = input("Nuevo nombre: ")
                    if nuevo != "":
                        art["nombre"] = nuevo
                    nuevo_p = input("Nuevo precio (vacío = igual): ")
                    if nuevo_p != "":
                        art["precio"] = float(nuevo_p)
                    nuevo_s = input("Nuevo stock (vacío = igual): ")
                    if nuevo_s != "":
                        art["stock"] = int(nuevo_s)

            if op_a == 5:
                id_e = int(input("ID: "))
                i = 0
                pos = -1
                while i < len(articulos):
                    if articulos[i]["id"] == id_e:
                        pos = i
                    i = i + 1
                if pos == -1:
                    print("No encontrado")
                else:
                    del articulos[pos]
                    print("Eliminado")

    if opcion == 3:
        op_v = 0
        while op_v != 8:
            print()
            print("--- MENÚ VENTAS / CARRITO ---")
            print("1. Seleccionar usuario")
            print("2. Añadir artículo al carrito")
            print("3. Quitar artículo del carrito")
            print("4. Ver carrito")
            print("5. Confirmar compra")
            print("6. Historial de ventas por usuario")
            print("7. Vaciar carrito")
            print("8. Volver")
            op_v = int(input("Opción: "))

            if op_v == 1:
                id_u = int(input("ID de usuario: "))
                i = 0
                usr = None
                while i < len(usuarios):
                    if usuarios[i]["id"] == id_u and usuarios[i]["activo"]:
                        usr = usuarios[i]
                    i = i + 1
                if usr == None:
                    print("Usuario no encontrado o inactivo")
                else:
                    usuario_activo = usr["id"]
                    print("Usuario activo:", usr["nombre"])

            if op_v == 2:
                if usuario_activo == None:
                    print("Primero selecciona usuario activo.")
                else:
                    id_art_c = int(input("ID del artículo: "))
                    i = 0
                    art = None
                    while i < len(articulos):
                        if articulos[i]["id"] == id_art_c and articulos[i]["activo"]:
                            art = articulos[i]
                        i = i + 1
                    if art == None:
                        print("Artículo no encontrado o inactivo")
                    else:
                        cant = int(input("Cantidad: "))
                        if cant <= art["stock"] and cant > 0:
                            j = 0
                            en_carrito = False
                            while j < len(carrito):
                                if carrito[j][0] == id_art_c:
                                    carrito[j] = (carrito[j][0], carrito[j][1] + cant)
                                    en_carrito = True
                                j = j + 1
                            if en_carrito == False:
                                carrito.append((id_art_c, cant))
                            print("Agregado al carrito")
                        else:
                            print("Cantidad inválida o sin stock")

            if op_v == 3:
                id_quit = int(input("ID artículo: "))
                i = 0
                pos = -1
                while i < len(carrito):
                    if carrito[i][0] == id_quit:
                        pos = i
                    i = i + 1
                if pos == -1:
                    print("No está en el carrito")
                else:
                    del carrito[pos]
                    print("Quitado")

            if op_v == 4:
                print("Carrito:")
                total = 0
                i = 0
                while i < len(carrito):
                    id_a = carrito[i][0]
                    cant = carrito[i][1]
                    j = 0
                    art = None
                    while j < len(articulos):
                        if articulos[j]["id"] == id_a:
                            art = articulos[j]
                        j = j + 1
                    if art != None:
                        sub = cant * art["precio"]
                        total = total + sub
                        print(art["nombre"], "x", cant, "=", sub)
                    i = i + 1
                print("Total:", total)

            if op_v == 5:
                if usuario_activo == None:
                    print("No hay usuario activo")
                elif len(carrito) == 0:
                    print("Carrito vacío")
                else:
                    items = []
                    total = 0
                    i = 0
                    ok = True
                    while i < len(carrito):
                        id_a = carrito[i][0]
                        cant = carrito[i][1]
                        j = 0
                        art = None
                        while j < len(articulos):
                            if articulos[j]["id"] == id_a:
                                art = articulos[j]
                            j = j + 1
                        if art == None or art["stock"] < cant or art["activo"] == False:
                            ok = False
                        i = i + 1
                    if ok == False:
                        print("Error: stock insuficiente o artículo inactivo")
                    else:
                        i = 0
                        while i < len(carrito):
                            id_a = carrito[i][0]
                            cant = carrito[i][1]
                            j = 0
                            art = None
                            while j < len(articulos):
                                if articulos[j]["id"] == id_a:
                                    art = articulos[j]
                                j = j + 1
                            art["stock"] = art["stock"] - cant
                            items.append((id_a, cant, art["precio"]))
                            total = total + cant * art["precio"]
                            i = i + 1
                        venta = {"id_venta": id_venta, "usuario_id": usuario_activo, "items": items, "total": total}
                        ventas.append(venta)
                        id_venta = id_venta + 1
                        carrito = []
                        print("Compra realizada, total:", total)

            if op_v == 6:
                id_u = int(input("ID usuario: "))
                i = 0
                print("Ventas de usuario", id_u)
                while i < len(ventas):
                    if ventas[i]["usuario_id"] == id_u:
                        print(ventas[i])
                    i = i + 1

            if op_v == 7:
                carrito = []
                print("Carrito vaciado")

print()
print("Programa terminado.")




