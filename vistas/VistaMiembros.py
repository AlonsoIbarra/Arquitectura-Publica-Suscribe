#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import getpass
import hashlib
import random
from contexto.Miembro import Miembro
from datos.ListaDeMiembros import ListaDeMiembros


class VistaMiembros():

    def menuMiembros(self):
        lu = ListaDeMiembros()
        while True:
            os.system('clear')
            print('')
            print('+---------------------------------------------+')
            print('|               MENÚ MIEMBROS                 |')
            print('+---------------------------------------------+')
            print('|  1.-  AGREGAR MIEMBRO                       |')
            print('+---------------------------------------------+')
            print('|  2.-  ELIMIAR MIEMBRO                       |')
            print('+---------------------------------------------+')
            print('|  3.-  LISTAR MIEMBROS                       |')
            print('+---------------------------------------------+')
            print('|  4.-  ASIGNAR MIEMBROS A GRUPOS             |')
            print('+---------------------------------------------+')
            print('|  5.-  REGRESAR                              |')
            print('+---------------------------------------------+')
            op = self.readInt("Ingrese opción: ")

            if op == 1:
                self.agregarMiembros(lu)
            elif op == 2:
                self.eliminarMiembros(lu)
            elif op == 3:
                self.listarMiembros(lu)
            elif op == 6:
                print "regresando..."
                break
            else:
                pass

    def listarMiembros(self, lu):
        os.system('clear')
        print('+-------------------------------------------------------+')
        print('|  ID  |  NOMBRES         |  APELLIDOS        |  EDAD   |')
        for u in lu.obtenerMiembros():
            print('+---------------------------------------------------+')
            print('|  ' + str(u.idMiembro) + '  | ' + str(u.nombres) + ' | ' + str(u.apellidos) + ' | ' + str(u.edad) + ' | ')
        print('+-------------------------------------------------------+')
        raw_input()
        return True

    def agregarMiembros(self, lu):
        os.system('clear')
        nombre = raw_input('Ingresa los nombres del miembro: ')
        apellidos = raw_input('Ingresa los apellidos del miembro: ')
        edad = raw_input('Ingresa la edad del miembro: ')
        miembro = Miembro()
        miembro.nombres = nombre
        miembro.apellidos = apellidos
        miembro.edad = int(edad)
        miembro.IDsTemperatura = random.randint(1000, 9999)
        miembro.IDsAcelerometro = random.randint(1000, 9999)
        miembro.IDsRitmoCardiaco = random.randint(1000, 9999)
        miembro.IDsPresion = random.randint(1000, 9999)
        if lu.agregarMiembro(miembro):
            print ('Miembro agregado exitosamente.')
            raw_input()
            return True
        else:
            print ('No se agrego el registro, intente nuevamente.')
            raw_input()
            return False

    def eliminarMiembros(self, lu):
        id = raw_input("Ingrese id del miembro: ")
        try:
            miembro = lu.obtenerMiembroPorId(id)
        except:
            print ('No se localizó el registro con id ' + str(id))
            raw_input()
            return False
        if str(raw_input('Confirma eliminar a ' + miembro.nombres + '? s/n  ')) == str('s'):
            try:
                if(lu.eliminarMiembro(miembro)):
                    print ('miembro ' + miembro.nombres + ' eliminado.')
                    raw_input()
                    return True
                else:
                    print ('No se pudo eliminar a ' + miembro.nombre + '.')
                    raw_input()
                    return False
            except:
                print ('No se pudo eliminar a ' + miembro.nombre + '.')
                raw_input()
                return False
        else:
            print ("Operacion cancelada")
            raw_input()

    def readInt(self, msg):
        try:
            return int(raw_input(msg))
        except ValueError:
            print "ERROR: Valor no numerico entero..."
            raw_input('')
            return -1
