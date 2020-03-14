# -*-coding: utf8-*-
# Programa: estacionamiento.py
# Objetivo: Crear una simulacion de un
#           estacionamiento de vehiculos
# Autor: Owen Ariel Valle Turcios
# Fecha: 13/03/2020
import sys
import platform
import datetime
import random

class menu_estacionamiento:
    """
    Despliega las opciones del estacionamiento
    """

    def __init__(self):
            """ Inicializa las listas de los vehiculos al dia """
            self.Vehiculo = list() #Lista de los vehiculos
        
            self.options = {"1":self.ingresovehiculo,
                            "2":self.totalvehiculos,
                            "3":self.salidasvehiculos,
                            "4":self.gananciasdeldia,
                            "5":self.salir
                            }

    def menu_principal(self):
        """ Despliega el menu de ingreso de vehiculos"""
        print("""
             
                Estacionamiento...

            1:Ingreso de vehiculos
            2:Total de vehiculos Estacionados
            3:Salidas
            4:Ganancias del dia
            5:Salir
             """)

    def ingreso_vehiculo(self):
        placa = input("Ingrese la placa del vehiculo: ")
        marca = input("Ingrese la marca del vehiculo: ")
        modelo = input("Ingrese el modelo del vehiculo: ")
        tipo = input("Ingrese tipo del vehiculo: ")
        hora_ingreso = input("Ingrese la hora de ingreso del vehiculo: ")
        estado = input("Estado por defecto True: ")
        print("El vehiculo se ingreso correctamente")
        pass

    def totalVehiculos(self):
 
        for vehi in vehiculos:
            print("placa: {0}\nmarca: '{1}'\nmodelo: {2}\ntipo: {3}"
                  .format())



    def salida(self):
         pass

    def gananciasDia(self):
         pass

    def salir(self):
          """ Cierra la aplicación """
          print("Gracias por utilizar nuestro servicio")
          sys.exit(0)

    def horas(self):
      horas_vehiculo=random(1,5)
      print(horas_vehiculo)
   if __name__ == "__main__":
    

        