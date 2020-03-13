# -*-coding: utf8-*-
# Programa: estacionamiento.py
# Objetivo: Crear una simulacion de un
#           estacionamiento de vehiculos
# Autor: Owen Ariel Valle Turcios
# Fecha: 13/03/2020
import sys
import platform
import os

class estacionamiento_vehiculo:
    """
    Despliega el menu para realizar la insercion de los datos
    """
    def __init__(self, placavehiculo,  marca, modelo, tipo):
        """Inicializa la insercion de los datos del vehiculo"""
        self.placavehiculo = placavehiculo
        self.marca = marca
        self.modelo = modelo
        print("Ingrese los datos del vehiculo:")
        
    def limpiar_pantalla(self):
          os.system("cls")
    
    def press_enter(self):
      """ Realiza una pausa y solicita presionar una tecla """
      input("\nPresiona Enter para continuar")

    def parqueo(self):
        """ Calcula el tiempo que lleva el vehiculo"""
        