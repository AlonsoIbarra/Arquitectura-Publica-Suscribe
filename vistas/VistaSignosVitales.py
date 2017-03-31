#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from contexto.Signo import Signo
from datos.ListaDeSignos import ListaDeSignos


class VistaSignosVitales():

    def menuSignosVitales(self):
        ls = ListaDeSignos()
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
                self.ActualizarTemperatura(ls)
            elif op == 2:
                pass
            elif op == 3:
                pass
            elif op == 6:
                print "regresando..."
                break
            else:
                pass

    def ActualizarTemperatura(self, ls):
        try:
            signo = ls.obtenerSignoPorDescripcion('Temperatura')
        except:
            print ('Registro no encontrado en base de datos.')
            return False
        print('+---------------------------------------------+')
        print('|      MÁXIMO         |       MINIMO         |')
        print('+---------------------------------------------+')
        print('+        ' + str(signo.max) + '           |         ' + str(signo.max) + '         |' )
        print('+---------------------------------------------+')
        max = self.readInt("Ingrese máximo: ")
        if max == -1:
            print('Ocurrio un error, cancelando')
            raw_input()
            return False
        min = self.readInt("Ingrese mínimo: ")
        if min == -1:
            print('Ocurrio un error, cancelando')
            raw_input()
            return False
        signo.max = max
        signo.min = min
        if (ls.actualizarSigno(signo)):
            print ('Valores de temperatura actualizos correctamente.')
            return True
        else:
            print ('Valores de temperatura no actualizos.')
            return True

    def readInt(self, msg):
        try:
            return int(raw_input(msg))
        except ValueError:
            print "ERROR: Valor no numerico entero..."
            raw_input('')
            return -1
