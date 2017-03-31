#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import getpass
import hashlib
import random
from contexto.Miembro import Miembro
from datos.ListaDeMiembros import ListaDeMiembros
from datos.ListaDeGrupos import ListaDeGrupos
from datos.ListaDeMedicamentos import ListaDeMedicamentos


class VistaMiembros():

    def menuMiembros(self):
        lu = ListaDeMiembros()
        while True:
            os.system('clear')
            print('')
            print('+---------------------------------------------+')
            print('|               MENÚ MIEMBROS                 |')
            print('+---------------------------------------------+')
            print('|  1.-  AGRAGAR MIEMBRO                       |')
            print('+---------------------------------------------+')
            print('|  2.-  ELIMIAR MIEMBRO                       |')
            print('+---------------------------------------------+')
            print('|  3.-  LISTAR MIEMBROS                       |')
            print('+---------------------------------------------+')
            print('|  4.-  ASIGNAR MIEMBROS A GRUPOS             |')
            print('+---------------------------------------------+')
            print('|  5.-  LISTAR MIEMBROS EN GRUPOS             |')
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
            elif op == 4:
                self.agregarMiembrosGrupos(lu)
            elif op == 5:
                self.listarMiembrosGrupos(lu)
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

    def listarMiembrosGrupos(self, lu):
        os.system('clear')
        temp=0
        for u in lu.obtenerMiembroGrupo():
            if(u[0]!=temp):
                temp=u[0]
                print('+-------------------------------------------------------+')
                print('|  GRUPO  |  MEDICAMENTO                                |')
                print('+-------------------------------------------------------+')
                print('| ' + str(u[0])+ ' |  ' + u[2] + ' ')
                print('+-------------------------------------------------------+')
                print('|  NOMBRE                              |  DOSIS         |')       
                print('+-------------------------------------------------------+')
            print('|  ' + u[1] + '  | ' + str(u[3]) + ' | ')
        print('+-------------------------------------------------------+')
        print(' ')
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

    def agregarMiembrosGrupos(self, lu):
        os.system('clear')
        id = raw_input('Ingresa el id del miembro: ')
        try:
            miembro = lu.obtenerMiembroPorId(id)
        except:
            print ('No se localizó el registro con id ' + str(id))
            raw_input()
            return False
        print('Miembro: ' + miembro.nombres)
        grupo = raw_input('Ingresa el id del grupo: ')
        try:
            lg = ListaDeGrupos()
            lm = ListaDeMedicamentos()
            grupo = lg.obtenerGrupoPorId(grupo)
            medicamento = lm.obtenerMedicamentoPorId(grupo.idMedicamento)
        except:
            print ('No se localizó el registro con id ' + str(id))
            raw_input()
            return False
        print('Medicamento: ' + medicamento.descripcion)
        dosis = raw_input('Ingresa la dosis: ')
        if str(raw_input('Confirma asignar a ' + miembro.nombres + ' al grupo ' + str(grupo.idGrupo) + ' con dosis ' + str(dosis) + '? s/n  ')) == str('s'):
            if lu.agregarMiembroGrupo(miembro.idMiembro, grupo.idGrupo, str(dosis)):
                print ('Miembro agregado a grupo exitosamente.')
                raw_input()
                return True
            else:
                print ('No se agrego el registro, intente nuevamente.')
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
