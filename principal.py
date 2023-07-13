from core import CitasManager

def mostrar_menu():
    print("----- Menú -----")
    print("1. Agregar cita")
    print("2. Buscar cita")
    print("3. Modificar cita")
    print("4. Cancelar cita")
    print("5. Salir del programa")

def agregar_cita(citas_manager):
    print("---- Agregar Cita ----")
    nombre = input("Nombre del paciente: ")
    fecha = input("Fecha de la cita: ")
    hora = input("Hora de la cita: ")
    motivo = input("Motivo de la consulta: ")

    cita = {
        'nombre': nombre,
        'fecha': fecha,
        'hora': hora,
        'motivo': motivo
    }

    citas_manager.agregar_cita(cita)
    print("Cita agregada exitosamente.")

def buscar_cita(citas_manager):
    print("---- Buscar Cita ----")
    criterio = input("Ingrese el criterio de búsqueda (nombre o fecha): ")

    citas_encontradas = citas_manager.buscar_citas(criterio)
    if citas_encontradas:
        print("Citas encontradas:")
        for cita in citas_encontradas:
            print(f"Nombre: {cita['nombre']}, Fecha: {cita['fecha']}, Hora: {cita['hora']}, Motivo: {cita['motivo']}")
    else:
        print("No se encontraron citas.")

def modificar_cita(citas_manager):
    print("---- Modificar Cita ----")
    fecha = input("Ingrese la fecha de la cita a modificar: ")
    hora = input("Ingrese la hora de la cita a modificar: ")

    for cita in citas_manager.citas:
        if cita['fecha'] == fecha and cita['hora'] == hora:
            nuevo_nombre = input("Ingrese el nuevo nombre del paciente: ")
            nuevo_motivo = input("Ingrese el nuevo motivo de la consulta: ")

            cita_modificada = {
                'nombre': nuevo_nombre,
                'fecha': cita['fecha'],
                'hora': cita['hora'],
                'motivo': nuevo_motivo
            }

            if citas_manager.modificar_cita(cita_modificada):
                print("Cita modificada exitosamente.")
            else:
                print("No se pudo modificar la cita.")
            return

    print("No se encontró la cita especificada.")

def cancelar_cita(citas_manager):
    print("---- Cancelar Cita ----")
    fecha = input("Ingrese la fecha de la cita a cancelar: ")
    hora = input("Ingrese la hora de la cita a cancelar: ")

    for cita in citas_manager.citas:
        if cita['fecha'] == fecha and cita['hora'] == hora:
            if citas_manager.cancelar_cita(cita):
                print("Cita cancelada exitosamente.")
            else:
                print("No se pudo cancelar la cita.")
            return

    print("No se encontró la cita especificada.")

def main():
    citas_manager = CitasManager('citas.json')

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            agregar_cita(citas_manager)
        elif opcion == '2':
            buscar_cita(citas_manager)
        elif opcion == '3':
            modificar_cita(citas_manager)
        elif opcion == '4':
            cancelar_cita(citas_manager)
        elif opcion == '5':
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

if __name__ == '__main__':
    main()

