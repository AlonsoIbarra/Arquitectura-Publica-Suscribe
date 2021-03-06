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
from vistas.VistaUsuarios import VistaUsuarios
from vistas.VistaGrupos import VistaGrupos
from vistas.VistaMedicamentos import VistaMedicamentos
from vistas.VistaSignosVitales import VistaSignosVitales
from vistas.VistaMiembros import VistaMiembros
from contexto.Usuario import Usuario
from datos.ListaDeUsuarios import ListaDeUsuarios
from sensores.SensorTemperatura import SensorTemperatura
from sensores.SensorRitmoCardiaco import SensorRitmoCardiaco
from sensores.SensorPresion import SensorPresion
from sensores.SensorAcelerometro import SensorAcelerometro
from datos.ListaDeMiembros import ListaDeMiembros
from datos.ListaDeSignos import ListaDeSignos
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
        return True

    def login(self):
        os.system('clear')
        print('+---------------------------------------------+')
        print('|                  Login                      |')
        print('+---------------------------------------------+')
        print('')
        usuarioNombre = raw_input("Ingrese Nombre de Usuario: ")
        pswd = getpass.getpass('Password:')
        usuario = self.obtenerUsuario(usuarioNombre)
        if isinstance(usuario, Usuario):
            if hashlib.sha224(pswd).hexdigest() == usuario.contrasena:
                if(int(usuario.tipo) == 1):
                    self.menuAdministrador()
                elif(int(usuario.tipo) == 2):
                    self.menuUsuario()
                else:
                    print('No se entontro el tipo de usuario, saliendo...')
                    raw_input()
                    return False
            else:
                print('Contraseña incorrecta, saliendo...')
                raw_input()
                return False
        else:
            print ('Nombre incorrecto, saliendo...')
            raw_input()
            return False

    def obtenerUsuario(self, usuarioNombre):
        lu = ListaDeUsuarios()
        try:
            return lu.obtenerUsuarioPorNombre(usuarioNombre)
        except:
            return None

    def menuUsuario(self):
        while True:
            os.system('clear')
            print('')
            print('+---------------------------------------------+')
            print('|                 MENÚ INICIAL                |')
            print('+---------------------------------------------+')
            print('|  1.-  INICIAR SIMULACIÓN LOCAL              |')
            print('+---------------------------------------------+')
            print('|  2.-  INICIAR SENSORES REMOTOS              |')
            print('+---------------------------------------------+')
            print('|  3.-  INICIAR MANAGERS REMOTOS              |')
            print('+---------------------------------------------+')
            print('|  4.-  SALIR DE SIMULADOR                    |')
            print('+---------------------------------------------+')
            op = self.readInt("Ingrese opción: ")
            if op == 1:
                self.iniciarSimulacion(0)
            elif op == 2:
                self.iniciarSimulacion(1)
            elif op == 3:
                self.iniciarSimulacion(2)
            elif op == 4:
                print "saliendo..."
                os.system('clear')
                break
            else:
                pass

    def menuAdministrador(self):
        vu = VistaUsuarios()
        vg = VistaGrupos()
        vm = VistaMedicamentos()
        vsv = VistaSignosVitales()
        vmi = VistaMiembros()
        while True:
            os.system('clear')
            print('')
            print('+---------------------------------------------+')
            print('|                 MENÚ INICIAL                |')
            print('+---------------------------------------------+')
            print('|  1.-  GESTIÓN DE USUARIOS                   |')
            print('+---------------------------------------------+')
            print('|  2.-  GESTIÓN DE MIEMBROS                   |')
            print('+---------------------------------------------+')
            print('|  3.-  GESTIÓN DE GRUPOS                     |')
            print('+---------------------------------------------+')
            print('|  4.-  GESTIÓN DE MEDICAMENTOS               |')
            print('+---------------------------------------------+')
            print('|  5.-  GESTIÓN DE SIGNOS VITALES             |')
            print('+---------------------------------------------+')
            print('|  6.-  INICIAR SIMULACIÓN LOCAL              |')
            print('+---------------------------------------------+')
            print('|  7.-  INICIAR SENSORES REMOTOS              |')
            print('+---------------------------------------------+')
            print('|  8.-  INICIAR MANAGERS REMOTOS              |')
            print('+---------------------------------------------+')
            print('|  9.-  SALIR DE SIMULADOR                    |')
            print('+---------------------------------------------+')
            op = self.readInt("Ingrese opción: ")
            if op == 1:
                vu.menuUsuarios()
            elif op == 2:
                vmi.menuMiembros()
            elif op == 3:
                vg.menuGrupos()
            elif op == 4:
                vm.menuMedicamentos()
            elif op == 5:
                vsv.menuSignosVitales()
            elif op == 6:
                print "iniciando simulación..."
                self.iniciarSimulacion(0)
            elif op == 7:
                self.iniciarSimulacion(1)
            elif op == 8:
                self.iniciarSimulacion(2)
            elif op == 9:
                print "saliendo..."
                os.system('clear')
                break
            else:
                pass

    def __pedirDatosRabbitMQRemoto(self):
        ipRabbit = raw_input('Ingrese IP remota del servidor de RabbitMQ ')
        if ipRabbit == '':
            return []
        usuarioRabbit = raw_input('Ingrese nombre de usuario de RabbitMQ ')
        if usuarioRabbit == '':
            return []
        pswRabbit = raw_input('Ingrese contraseña de servidor de RabbitMQ ')
        if pswRabbit == '':
            return []
        access = [ipRabbit, usuarioRabbit, pswRabbit]
        return access

    def iniciarSimulacion(self, opt):
        datosRabbitMQ = []
        if int(opt) > 0:
            datosRabbitMQ = self.__pedirDatosRabbitMQRemoto()
            if datosRabbitMQ == []:
                return False
        lista = ListaDeMiembros()
        for usuario in lista.obtenerMiembros():
            self.create_temperature_sensor(usuario.nombres, datosRabbitMQ)
            self.create_heart_rate_sensor(usuario.nombres, datosRabbitMQ)
            self.create_preasure_sensor(usuario.nombres, datosRabbitMQ)
            self.create_acelerometer(usuario.nombres, datosRabbitMQ)
        if opt == 0:
            self.run_simulator()
        elif opt == 1:
            self.start_publishers()
        elif opt == 2:
            self.start_consumers(datosRabbitMQ)
        else:
            pass

    def create_temperature_sensor(self, nombre, datosRabbitMQ):
        s = SensorTemperatura(nombre, datosRabbitMQ)
        self.sensores.append(s)

    def create_preasure_sensor(self, nombre, datosRabbitMQ):
        s = SensorPresion(nombre, datosRabbitMQ)
        self.sensores.append(s)

    def create_heart_rate_sensor(self, nombre, datosRabbitMQ):
        s = SensorRitmoCardiaco(nombre, datosRabbitMQ)
        self.sensores.append(s)

    def create_acelerometer(self, nombre, datosRabbitMQ):
        s = SensorAcelerometro(nombre, datosRabbitMQ)
        self.sensores.append(s)

    def run_simulator(self):
        self.start_consumers([])
        self.start_publishers()

    def start_consumers(self, dataRabbitMQ):
        ls = ListaDeSignos()
        try:
            temperatura = ls.obtenerSignoPorDescripcion('Temperatura')
            ritmo = ls.obtenerSignoPorDescripcion('Ritmo')
            presion = ls.obtenerSignoPorDescripcion('Presion')
        except:
            print ('No se tienen registrados todos los valores máximos de signos vitales, seleccione opción 5 para actualizar valores.')
            raw_input()
            return False
        argumentos = " ".join(dataRabbitMQ)
        os.system(
            "gnome-terminal -e 'bash -c \"python " + os.path.abspath("\managers") + "/TemperaturaManager.py " + str(temperatura.max) + "  " + str(argumentos) + " ; sleep 5 \"'")
        os.system(
            "gnome-terminal -e 'bash -c \"python " + os.path.abspath("\managers") + "/RitmoCardiacoManager.py " + str(ritmo.max) + "  " + str(argumentos) + " ; sleep 5 \"'")
        os.system(
            "gnome-terminal -e 'bash -c \"python " + os.path.abspath("\managers") + "/PresionManager.py " + str(presion.max) + "  " + str(argumentos) + " ; sleep 5 \"'")
        os.system(
            "gnome-terminal -e 'bash -c \"python " + os.path.abspath("\managers") + "/AcelerometroManager.py " + str(argumentos) + " ; sleep 5 \"'")
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
