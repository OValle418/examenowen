# -*-coding: utf8-*-
# Programa: ingreso_vehiculo_nuevo
# Objetivo: Crear una simulacion de un
#           estacionamiento de vehiculos
# Autor: Owen Ariel Valle Turcios
# Fecha: 13/03/2020

class Vehiculo():
    
    def __init__(self):
        """ Inicializa una lista vacía """
        self.vehiculos = list()

    def nuevo_vehiculo(self):
        """ Crea una nueva nota y la agrega a memo """
        self.vehiculos.append(Note(memo, tags))

    def _search_note(self, note_id):
        """
        Busca una nota con el id enviado.
        """
            for note in self.notes:
            if str(note.id) == str(note_id):
                return note

        return None