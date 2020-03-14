# -*-coding: utf8-*-
# Programa: estacionamiento.py
# Objetivo: Crear una simulacion de un
#           estacionamiento de vehiculos
# Autor: Owen Ariel Valle Turcios
# Fecha: 13/03/2020
class Vehiculo:
    """
    representa un vehiculo
    """

    def __init__(self, placa, modelo, marca, tipo):
        """ """
        self.placa = placa
        self.modelo = modelo
        self.marca = marca
        self.tipo = tipo
        