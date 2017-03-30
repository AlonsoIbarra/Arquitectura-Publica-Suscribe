#!/usr/bin/env python
# -*- coding: utf-8 -*-
# --------------------------------------------------------------------------------------------------
# Archivo: Simulador.py
# Capitulo: 3 Estilo Publica-Subscribe
# Autor(es): Perla Velasco & Yonathan Mtz.
# Version: 1.2 Agosto 2016
# Descripción:
#
#   Ésta clase define el rol de set-up del proyecto y permite instanciar las clases para
#   construir un entorno simulado del caso de estudio.
#
#   Las características de ésta clase son las siguientes:
#
#                                        Simulador.py
#           +-----------------------+-------------------------+------------------------+
#           |  Nombre del elemento  |     Responsabilidad     |      Propiedades       |
#           +-----------------------+-------------------------+------------------------+
#           |                       |                         |  - Inicializa los pu-  |
#           |                       |                         |    blicadores y los    |
#           |                       |                         |    subscriptores.      |
#           |        Set-Up         |  - Levantar entorno de  |  - Solicita al usuario |
#           |                       |    simulación.          |    las características |
#           |                       |                         |    con las que contará |
#           |                       |                         |    la simulación a eje-|
#           |                       |                         |    cutar.              |
#           +-----------------------+-------------------------+------------------------+
#
#   A continuación se describen los métodos que se implementaron en ésta clase:
#
#                                             Métodos:
#           +-------------------------+--------------------------+-----------------------+
#           |         Nombre          |        Parámetros        |        Función        |
#           +-------------------------+--------------------------+-----------------------+
#           |                         |                          |  - Solicita al usua-  |
#           |                         |                          |    rio los valores    |
#           |                         |                          |    necesarios para i- |
#           |                         |                          |    nicializar la si-  |
#           |                         |                          |    mulación.          |
#           |         main()          |           None           |  - Manda crear los    |
#           |                         |                          |    publicadores.      |
#           |                         |                          |  - Manda crear los    |
#           |                         |                          |    subscriptores.     |
#           |                         |                          |  - Solicita los valo- |
#           |                         |                          |    res máximos que    |
#           |                         |                          |    generarán los      |
#           |                         |                          |    eventos.           |
#           +-------------------------+--------------------------+-----------------------+
#           |   create_temperature    |     String: nombre       |  - Instancia la clase |
#           |        _sensor()        |                          |    SensorTemperatura. |
#           +-------------------------+--------------------------+-----------------------+
#           |     create_preasure     |     String: nombre       |  - Instancia la clase |
#           |        _sensor()        |                          |    SensorPresion.     |
#           +-------------------------+--------------------------+-----------------------+
#           |    create_heart_rate    |     String: nombre       |  - Instancia la clase |
#           |        _sensor()        |                          |    SensorRitmoCardiaco|
#           +-------------------------+--------------------------+-----------------------+
#           |                         |                          |  - Ejecuta los metodos|
#           |    run_simulator()      |           None           |    que inician a los  |
#           |                         |                          |    subscriptores y a  |
#           |                         |                          |    los publicadores.  |
#           +-------------------------+--------------------------+-----------------------+
#           |                         |                          |  - Abre tres termina- |
#           |    start_consumers()    |           None           |    les y en cada una  |
#           |                         |                          |    de ellas ejecuta un|
#           |                         |                          |    subscriptor.       |
#           +-------------------------+--------------------------+-----------------------+
#           |                         |                          |  - Simula 1000 eventos|
#           |    start_publishers()   |           None           |    generados por los  |
#           |                         |                          |    sensores.          |
#           +-------------------------+--------------------------+-----------------------+
#
# -------------------------------------------------------------------------------------------------

import os
from sensores.SensorTemperatura import SensorTemperatura
from sensores.SensorRitmoCardiaco import SensorRitmoCardiaco
from sensores.SensorPresion import SensorPresion
from sensores.SensorAcelerometro import SensorAcelerometro
from datos.ListaDeMiembros import ListaDeMiembros
from contexto.Medicamento import Medicamento
from datos.ListaDeMedicamentos import ListaDeMedicamentos
import getpass
import hashlib
import time


class SetUpSimulador:
    sensores = []
    temperatura = 0
    ritmo_cardiaco = 0
    presion = 0

    def readInt(self, msg):
        try:
            return int(raw_input(msg))
        except ValueError:
            print "ERROR: Valor no numerico entero..."
            raw_input('')
            return -1

    def main(self):
        print('+---------------------------------------------+')
        print('|  Bienvenido al Simulador Publica-Subscribe  |')
        print('+---------------------------------------------+')
        print('')
        raw_input('presiona enter para continuar: ')
        os.system('clear')
        print('')
        print('+---------------------------------------------+')
        print('|        Evento        |      Descripción     |')
        print('+---------------------------------------------+')
        print('|                      |   - La temperatura   |')
        print('|       Calentura      |     corporal supera  |')
        print('|                      |     los 38°.         |')
        print('+----------------------+----------------------+')
        print('|                      |   - Presión excesiva-|')
        print('|                      |     mente alta de la |')
        print('|     Hipertensión     |     sangre sobre la  |')
        print('|                      |     pared de las ar- |')
        print('|                      |     terias.          |')
        print('+----------------------+----------------------+')
        print('|     Taquicardia      |   - Velocidad excesi-|')
        print('|                      |     va del ritmo de  |')
        print('|                      |     los latidos del  |')
        print('|                      |     corazón.         |')
        print('+----------------------+----------------------+')
        print('|     Caida            |   - la posicion de   |')
        print('|                      |     orizontal es     |')
        print('|                      |     correspondiente  |')
        print('|                      |     a una caida      |')
        print('+----------------------+----------------------+')
        print('')
        raw_input('presiona enter para continuar: ')
        self.login()

    def login(self):
        print('+---------------------------------------------+')
        print('|                  Login                      |')
        print('+---------------------------------------------+')
        print('')
        usuario = raw_input("Ingrese Nombre de Usuario: ")
        pswd = getpass.getpass('Password:')
        user = self.getUser(usuario)
        if hashlib.sha224(pswd).hexdigest() == user[3]:
            if(int(user[2]) == 0):
                self.menuAdministrador()
            else:
                self.menuUsuario()

    def getUser(self, usuario):
        return (1, 'usuario', 0, '147ad31215fd55112ce613a7883902bb306aa35bba879cd2dbe500b9')

    def menuUsuario(self):
        while True:
            os.system('clear')
            print('')
            print('+---------------------------------------------+')
            print('|                 MENÚ INICIAL                |')
            print('+---------------------------------------------+')
            print('|  1.-  INICIAR SIMULACIÓN                    |')
            print('+---------------------------------------------+')
            print('|  2.-  SALIR DE SIMULADOR                    |')
            print('+---------------------------------------------+')
            op = self.readInt("Ingrese opción: ")
            if op == 1:
                print "iniciando simulación..."
                self.iniciarSimulacion()
            elif op == 2:
                print "saliendo..."
                os.system('clear')
                break
            else:
                pass

    def menuAdministrador(self):
        while True:
            os.system('clear')
            print('')
            print('+---------------------------------------------+')
            print('|                 MENÚ INICIAL                |')
            print('+---------------------------------------------+')
            print('|  1.-  GESTIÓN DE USUARIOS                   |')
            print('+---------------------------------------------+')
            print('|  2.-  GESTIÓN DE GRUPOS                     |')
            print('+---------------------------------------------+')
            print('|  3.-  GESTIÓN DE MEDICAMENTOS               |')
            print('+---------------------------------------------+')
            print('|  4.-  GESTIÓN DE SIGNOS VITALES             |')
            print('+---------------------------------------------+')
            print('|  5.-  INICIAR SIMULACIÓN                    |')
            print('+---------------------------------------------+')
            print('|  6.-  SALIR DE SIMULADOR                    |')
            print('+---------------------------------------------+')
            op = self.readInt("Ingrese opción: ")
            if op == 1:
                self.menuUsuarios()
            elif op == 2:
                self.menuGrupos()
            elif op == 3:
                self.menuMedicamentos()
            elif op == 4:
                self.menuSignosVitales()
            elif op == 5:
                print "iniciando simulación..."
                self.iniciarSimulacion()
            elif op == 6:
                print "saliendo..."
                os.system('clear')
                break
            else:
                pass

    def menuUsuarios(self):
        while True:
            os.system('clear')
            print('')
            print('+---------------------------------------------+')
            print('|               MENÚ USUARIOS                 |')
            print('+---------------------------------------------+')
            print('|  1.-  AGRAGAR USUARIO                       |')
            print('+---------------------------------------------+')
            print('|  2.-  ELIMIAR USUARIO                       |')
            print('+---------------------------------------------+')
            print('|  6.-  REGRESAR                              |')
            print('+---------------------------------------------+')
            op = self.readInt("Ingrese opción: ")

            if op == 1:
                print('')
                nombre = raw_input("Ingrese Nombre: ")
                edad = self.readInt("Ingrese Edad: ")
                self.registrarUsuario(nombre, edad)
                print "Registrando..."
            elif op == 2:
                nombre = raw_input("Ingrese nombre: ")
                self.eliminarUsuario(nombre)
                print "eliminando..."
            elif op == 6:
                print "regresando..."
                break
            else:
                pass

    def registrarUsuario(self, nombre, edad):
        pass

    def eliminarUsuario(self, nombre):
        pass

    def menuGrupos(self):
        while True:
            os.system('clear')
            print('')
            print('+---------------------------------------------+')
            print('|                 MENÚ GRUPOS                 |')
            print('+---------------------------------------------+')
            print('|  1.-  AGRAGAR USUARIO                       |')
            print('+---------------------------------------------+')
            print('|  2.-  ELIMIAR USUARIO                       |')
            print('+---------------------------------------------+')
            print('|  6.-  REGRESAR                              |')
            print('+---------------------------------------------+')
            op = self.readInt("Ingrese opción: ")
            if op == 1:
                pass
            elif op == 2:
                pass
            elif op == 3:
                pass
            elif op == 6:
                print "regresando..."
                break
            else:
                pass

    def menuMedicamentos(self):
        lm = ListaDeMedicamentos()
        while True:
            os.system('clear')
            print('')
            print('+---------------------------------------------+')
            print('|             MENÚ MEDICAMENTOS               |')
            print('+---------------------------------------------+')
            print('|  1.-  AGRAGAR MEDICAMENTO                   |')
            print('+---------------------------------------------+')
            print('|  2.-  ELIMIAR MEDICAMENTO                   |')
            print('+---------------------------------------------+')
            print('|  3.-  LISTAR MEDICAMENTOS                   |')
            print('+---------------------------------------------+')
            print('|  6.-  REGRESAR                              |')
            print('+---------------------------------------------+')
            op = self.readInt("Ingrese opción: ")
            if op == 1:
                self.agregarMedicamento(lm)
            elif op == 2:
                self.eliminarMedicamento(lm)
            elif op == 3:
                self.listarMedicamentos(lm)
            elif op == 6:
                print "regresando..."
                break
            else:
                pass

    def agregarMedicamento(self, lm):
        try:
            medicamento = Medicamento()
            medicamento.descripcion = raw_input('ingrese el nombre del medicamento ')
            lm.agregarMedicamento(medicamento)
            print ("Medicamento agragado exitosamente.")
            raw_input()
            return True
        except:
            print ("Ocurrio un problema, intente nuevamente.")
            raw_input()
            return False

    def eliminarMedicamento(self, lm):
        try:
            idMedicamento = self.readInt('Ingrese el id del medicamento. ')
            md = lm.obtenerMedicamentoPorId(idMedicamento)
        except:
            print ("Medicamento no encontrado")
            raw_input()
            return False
        if str(raw_input('confirma eliminar ' + md.descripcion + '? s/n  ')) == str('s'):
            try:
                lm.eliminarMedicamento(md)
                print ("Medicamento eliminado.")
                raw_input()
            except:
                print ("Fallo al eliminar medicamento.")
                raw_input()
        else:
            print ("Operacion cancelada")
            raw_input()

    def listarMedicamentos(self, lm):
        print('+---------------------------------------------+')
        print('|  ID  |  MEDICAMENTO                        |')
        print('+---------------------------------------------+')
        for m in lm.obtenerMedicamentos():
            print('|  ' + str(m[0]) + '  |  ' + str(m[1]) + '       |')
            print('+---------------------------------------------+')
        raw_input()

    def menuSignosVitales(self):
        while True:
            os.system('clear')
            print('')
            print('+---------------------------------------------+')
            print('|            MENÚ SIGNOS VITALES              |')
            print('+---------------------------------------------+')
            print('|  1.-  MODIFICAR TEMPERATURA                 |')
            print('+---------------------------------------------+')
            print('|  2.-  MODIFICAR PRESIÓN                     |')
            print('+---------------------------------------------+')
            print('|  3.-  MODIFICAR RITMO CARDIACO              |')
            print('+---------------------------------------------+')
            print('|  6.-  REGRESAR                              |')
            print('+---------------------------------------------+')
            op = self.readInt("Ingrese opción: ")

            if op == 1:
                print('')
                temp = self.readInt("Ingrese Temperatura: ")
                self.actualizarSV(id, temp)
                print "temperatura..."
            elif op == 2:
                temp = self.readInt("Ingrese Presión: ")
                self.actualizarSV(id, temp)
                print "presión..."
            elif op == 3:
                temp = self.readInt("Ingrese Ritmo Cardiaco: ")
                self.actualizarSV(id, temp)
                print "ritmo cardiaco..."
            elif op == 6:
                print "regresando..."
                break
            else:
                pass

    def actualizarSV(self, id, value):
        pass

    def iniciarSimulacion(self):
        lista = ListaDeMiembros()
        for usuario in lista.obtenerMiembros():
            self.create_temperature_sensor(usuario.nombres)
            self.create_heart_rate_sensor(usuario.nombres)
            self.create_preasure_sensor(usuario.nombres)
            self.create_acelerometer(usuario.nombres)
        self.run_simulator()

    def create_temperature_sensor(self, nombre):
        s = SensorTemperatura(nombre)
        self.sensores.append(s)

    def create_preasure_sensor(self, nombre):
        s = SensorPresion(nombre)
        self.sensores.append(s)

    def create_heart_rate_sensor(self, nombre):
        s = SensorRitmoCardiaco(nombre)
        self.sensores.append(s)

    def run_simulator(self):
        self.start_consumers()
        self.start_publishers()

    def create_acelerometer(self, nombre):
        s = SensorAcelerometro(nombre)
        self.sensores.append(s)

    def start_consumers(self):
        os.system(
            "gnome-terminal -e 'bash -c \"python " + os.path.abspath("\managers") + "/TemperaturaManager.py " + str(self.temperatura) + "; sleep 5 \"'")
        os.system(
            "gnome-terminal -e 'bash -c \"python " + os.path.abspath("\managers") + "/RitmoCardiacoManager.py " + str(self.ritmo_cardiaco) + "; sleep 5 \"'")
        os.system(
            "gnome-terminal -e 'bash -c \"python " + os.path.abspath("\managers") + "/PresionManager.py " + str(self.presion) + "; sleep 5 \"'")
        os.system(
            "gnome-terminal -e 'bash -c \"python " + os.path.abspath("\managers") + "/AcelerometroManager.py ; sleep 5 \"'")
        os.system(
            "gnome-terminal -e 'bash -c \"python TimerMedicamento.py ; sleep 5 \"'")

    def start_publishers(self):
        for x in xrange(0, 1000):
            for s in self.sensores:
                s.start_service()
                time.sleep(1.0)


if __name__ == '__main__':
    simulador = SetUpSimulador()
    simulador.main()
