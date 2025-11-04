from tabulate import tabulate

def generar_id(lista):
    """Genera un id incremental según los elementos existentes."""
    if not lista:
        return 1
    return max(e["id"] for e in lista) + 1

def leer_texto(mensaje):
    """Lee texto no vacío."""
    while True:
        texto = input(mensaje).strip()
        if texto:
            return texto
        print("  No puede estar vacío.")

def leer_int(mensaje, minimo=None, maximo=None):
    """Lee un entero con validación de rango."""
    while True:
        try:
            n = int(input(mensaje))
            if (minimo is not None and n < minimo) or (maximo is not None and n > maximo):
                print(f"  Debe estar entre {minimo} y {maximo}.")
            else:
                return n
        except ValueError:
            print("  Debes ingresar un número entero.")

def imprimir_tabla(filas, columnas):
    """Imprime una tabla usando tabulate."""
    if filas:
        print(tabulate(filas, headers=columnas, tablefmt="grid"))
    else:
        print("No hay datos para mostrar.")

# equipos

from utiles import generar_id, leer_texto, leer_int, imprimir_tabla

equipos = []  # lista global (solo memoria)

def menu_equipos():
    opcion = 0
    while opcion != 5:
        print("\n=== GESTIÓN DE EQUIPOS ===")
        print("1. Crear equipo")
        print("2. Listar equipos")
        print("3. Buscar equipo por ID")
        print("4. Actualizar/Eliminar equipo")
        print("5. Volver al menú principal")

        opcion = leer_int("Elige una opción: ", 1, 5)
        if opcion == 1:
            crear_equipo()
        elif opcion == 2:
            listar_equipos()
        elif opcion == 3:
            buscar_equipo()
        elif opcion == 4:
            actualizar_o_eliminar()

def crear_equipo():
    nombre = leer_texto("Nombre del equipo: ")
    ciudad = leer_texto("Ciudad: ")
    equipo = {"id": generar_id(equipos), "nombre": nombre, "ciudad": ciudad, "activo": True}
    equipos.append(equipo)
    print(" Equipo creado correctamente.")

def listar_equipos():
    activos = [e for e in equipos if e["activo"]]
    filas = [[e["id"], e["nombre"], e["ciudad"]] for e in activos]
    imprimir_tabla(filas, ["ID", "Nombre", "Ciudad"])

def buscar_equipo():
    id_buscar = leer_int("ID del equipo: ")
    for e in equipos:
        if e["id"] == id_buscar and e["activo"]:
            imprimir_tabla([[e["id"], e["nombre"], e["ciudad"]]], ["ID", "Nombre", "Ciudad"])
            return
    print(" Equipo no encontrado o inactivo.")

def actualizar_o_eliminar():
    id_buscar = leer_int("ID del equipo: ")
    for e in equipos:
        if e["id"] == id_buscar:
            print("1. Actualizar")
            print("2. Eliminar (marcar inactivo)")
            op = leer_int("Elige: ", 1, 2)
            if op == 1:
                e["nombre"] = leer_texto("Nuevo nombre: ")
                e["ciudad"] = leer_texto("Nueva ciudad: ")
                print(" Equipo actualizado.")
            else:
                e["activo"] = False
                print(" Equipo marcado como inactivo.")
            return
    print(" Equipo no encontrado.")

# jugadores

from utiles import generar_id, leer_texto, leer_int, imprimir_tabla
from equipos import equipos

jugadores = []

def menu_jugadores():
    opcion = 0
    while opcion != 5:
        print("\n=== GESTIÓN DE JUGADORES ===")
        print("1. Crear jugador")
        print("2. Listar jugadores")
        print("3. Buscar jugador")
        print("4. Actualizar/Eliminar jugador")
        print("5. Volver al menú principal")

        opcion = leer_int("Elige una opción: ", 1, 5)
        if opcion == 1:
            crear_jugador()
        elif opcion == 2:
            listar_jugadores()
        elif opcion == 3:
            buscar_jugador()
        elif opcion == 4:
            actualizar_o_eliminar()

def crear_jugador():
    nombre = leer_texto("Nombre del jugador: ")
    posicion = leer_texto("Posición: ")
    equipo_id = leer_int("ID del equipo: ")
    equipo = next((e for e in equipos if e["id"] == equipo_id and e["activo"]), None)
    if not equipo:
        print(" Equipo no válido o inactivo.")
        return
    jugador = {"id": generar_id(jugadores), "nombre": nombre, "posicion": posicion, "equipo_id": equipo_id, "activo": True}
    jugadores.append(jugador)
    print(" Jugador creado correctamente.")

def listar_jugadores():
    filas = []
    for j in jugadores:
        if j["activo"]:
            equipo = next((e["nombre"] for e in equipos if e["id"] == j["equipo_id"]), "Sin equipo")
            filas.append([j["id"], j["nombre"], j["posicion"], equipo])
    imprimir_tabla(filas, ["ID", "Nombre", "Posición", "Equipo"])

# menu

from equipos import menu_equipos
from jugadores import menu_jugadores

def main():
    opcion = 0
    while opcion != 5:
        print("\n=== LIGA DEPORTIVA AMATEUR ===")
        print("1. Gestión de equipos")
        print("2. Gestión de jugadores")
        print("3. Calendario de partidos")
        print("4. Resultados y clasificación")
        print("5. Salir")

        try:
            opcion = int(input("Elige una opción: "))
        except ValueError:
            opcion = 0

        if opcion == 1:
            menu_equipos()
        elif opcion == 2:
            menu_jugadores()
        elif opcion == 3:
            print(" Módulo de calendario en desarrollo.")
        elif opcion == 4:
            print(" Módulo de ranking en desarrollo.")
        elif opcion == 5:
            print(" Saliendo...")
        else:
            print(" Opción inválida.")

if __name__ == "__main__":
    main()
