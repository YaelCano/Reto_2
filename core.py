import json

class CitasManager:
    def __init__(self, archivo):
        self.archivo = archivo
        self.citas = self.cargar_citas()

    def cargar_citas(self):
        try:
            with open(self.archivo) as archivo_json:
                citas = json.load(archivo_json)
                return citas
        except FileNotFoundError:
            return []

    def guardar_citas(self):
        with open(self.archivo, 'w') as archivo_json:
            json.dump(self.citas, archivo_json)

    def agregar_cita(self, cita):
        self.citas.append(cita)
        self.guardar_citas()

    def buscar_citas(self, criterio):
        citas_encontradas = []
        for cita in self.citas:
            if criterio in cita.values():
                citas_encontradas.append(cita)
        return citas_encontradas

    def modificar_cita(self, cita_modificada):
        for i, cita in enumerate(self.citas):
            if cita['fecha'] == cita_modificada['fecha'] and cita['hora'] == cita_modificada['hora']:
                self.citas[i] = cita_modificada
                self.guardar_citas()
                return True
        return False

    def cancelar_cita(self, cita_cancelada):
        for i, cita in enumerate(self.citas):
            if cita['fecha'] == cita_cancelada['fecha'] and cita['hora'] == cita_cancelada['hora']:
                del self.citas[i]
                self.guardar_citas()
                return True
        return False
