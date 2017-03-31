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
                self.actualizarSignoVital(ls, "Temperatura")
            elif op == 2:
                self.actualizarSignoVital(ls, "Presion")
            elif op == 3:
                self.actualizarSignoVital(ls, "Ritmo")
            elif op == 6:
                print "regresando..."
                break
            else:
                pass

    def actualizarSignoVital(self, ls, pSigno):
        print (str(pSigno))
        try:
            signo = ls.obtenerSignoPorDescripcion(str(pSigno))
        except:
            signo = Signo()
            signo.descripcion = str(pSigno)
            signo.max = -1
            signo.min = -1
            ls.agregarSigno(signo)
            signo = ls.obtenerSignoPorDescripcion(str(pSigno))
        print('+---------------------------------------------+')
        print('|      MÁXIMO         |       MÍNIMO         |')
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
