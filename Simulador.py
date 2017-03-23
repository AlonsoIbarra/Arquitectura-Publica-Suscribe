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
# --------------------------------------------------------------------------------------------------

import os
from SensorTemperatura import SensorTemperatura
from SensorRitmoCardiaco import SensorRitmoCardiaco
from SensorPresion import SensorPresion
from SensorAcelerometro import SensorAcelerometro


class SetUpSimulador:
    sensores = []
    temperatura = 0
    ritmo_cardiaco = 0
    presion = 0

    def main(self):
        print('+---------------------------------------------+')
        print('|  Bienvenido al Simulador Publica-Subscribe  |')
        print('+---------------------------------------------+')
        print('')
        raw_input('presiona enter para continuar: ')
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
        print('')
        print('+---------------------------------------------+')
        print('|        CONFIGURACIÓN DE LA SIMULACIÓN       |')
        print('+---------------------------------------------+')
        print('|        Número de publicadores         |  ?  |')
        print('+---------------------------------------------+')
        publishers = raw_input('número entero: ')
        print('+---------------------------------------------+')
        print('|        Número de publicadores         |  ' + publishers + '  |')
        print('+---------------------------------------------+')
        print('|            ASIGNACIÓN DE SENSORES           |')
        print('+---------------------------------------------+')
        print('')
        raw_input('presiona enter para continuar: ')
        print('')
        for x in xrange(0, int(publishers)):
            print('+---------------------------------------------+')
            print('|            DATOS DEL ADULTO MAYOR |    ' + str(x) + '    |')
            print('+---------------------------------------------+')
            print('|           NOMBRE           |        ?       |')
            print('+---------------------------------------------+')
            nombre = raw_input('escribe el nombre: ')
            print('+---------------------------------------------+')
            print('|           NOMBRE           | ' + nombre + ' |')
            print('+---------------------------------------------+')
            self.create_temperature_sensor(nombre)
            print('|     SENSOR TEMPERATURA     |    ASIGNADO   |')
            print('+---------------------------------------------+')
            self.create_preasure_sensor(nombre)
            print('|       SENSOR PRESIÓN       |    ASIGNADO   |')
            print('+---------------------------------------------+')
            self.create_heart_rate_sensor(nombre)
            print('|    SENSOR RITMO CARDIACO   |    ASIGNADO   |')
            print('+---------------------------------------------+')
            self.create_acelerometer(nombre)
            print('|       SENSOR ACELEROMETRO       |    ASIGNADO   |')
            print('+---------------------------------------------+')
            print('')

            raw_input('presiona enter para continuar: ')
        print('+---------------------------------------------+')
        print('|        VALORES MÁXIMOS DE LOS EVENTOS       |')
        print('+---------------------------------------------+')
        print('|          TEMPERATURA       |        ?       |')
        print('+---------------------------------------------+')
        temperatura_maxima = raw_input('temperatura máxima: ')
        self.temperatura = int(temperatura_maxima)
        print('+---------------------------------------------+')
        print('|          TEMPERATURA       |       ' + temperatura_maxima + '       |')
        print('+---------------------------------------------+')
        print('|       RITMO CARDIACO       |        ?       |')
        print('+---------------------------------------------+')
        ritmo_maximo = raw_input('ritmo máximo: ')
        self.ritmo_cardiaco = int(ritmo_maximo)
        print('+---------------------------------------------+')
        print('|       RITMO CARDIACO       |      ' + ritmo_maximo + '       |')
        print('+---------------------------------------------+')
        print('|      PRESION ARTERIAL      |        ?       |')
        print('+---------------------------------------------+')
        presion_maxima = raw_input('presión máxima: ')
        self.presion = int(presion_maxima)
        print('+---------------------------------------------+')
        print('|      PRESION ARTERIAL      |      ' + presion_maxima + '       |')
        print('+---------------------------------------------+')
        print('|   CONFIGURACIÓN DE LA SIMULACIÓN TERMINADA  |')
        print('+---------------------------------------------+')
        raw_input('presiona enter para continuar: ')
        print('+---------------------------------------------+')
        print('|             INICIANDO SIMULACIÓN            |')
        print('+---------------------------------------------+')
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
            "gnome-terminal -e 'bash -c \"python TemperaturaManager.py " + str(self.temperatura) + "; sleep 5 \"'")
        os.system(
            "gnome-terminal -e 'bash -c \"python RitmoCardiacoManager.py " + str(self.ritmo_cardiaco) + "; sleep 5 \"'")
        os.system(
            "gnome-terminal -e 'bash -c \"python PresionManager.py " + str(self.presion) + "; sleep 5 \"'")
        os.system(
            "gnome-terminal -e 'bash -c \"python AcelerometroManager.py ; sleep 5 \"'")

    def start_publishers(self):
        for x in xrange(0, 1000):
            for s in self.sensores:
                s.start_service()


if __name__ == '__main__':
    simulador = SetUpSimulador()
    simulador.main()
