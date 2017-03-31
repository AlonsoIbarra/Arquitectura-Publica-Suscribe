#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import getpass
import hashlib
from contexto.Usuario import Usuario
from datos.ListaDeUsuarios import ListaDeUsuarios


class VistaUsuarios():

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
        nombre = raw_input('Ingresa el nombre del usuario: ')
        usuario = Usuario()
        pwd = getpass.getpass('Ingresa su contraseña: ')
        tipo = self.readInt('Ingresa el tipo de usuario [Administrador : 1 , Operador : 2 ] ')
        usuario.nombre = nombre
        usuario.contrasena = hashlib.sha224(pwd).hexdigest()
        usuario.tipo = tipo
        if lu.agregarUsuario(usuario):
            print ('Usuario agregado exitosamente.')
            raw_input()
            return True
        else:
            print ('No se agrego el registro, intente nuevamente.')
            raw_input()
            return False

    def eliminarMiembros(self, lu):
        nombre = raw_input("Ingrese nombre del usuario: ")
        try:
            usuario = lu.obtenerUsuarioPorNombre(nombre)
        except:
            print ('No se localizó el registro de ' + nombre)
            raw_input()
            return False
        if str(raw_input('Confirma eliminar a ' + nombre + '? s/n  ')) == str('s'):
            try:
                if(lu.eliminarUsuario(usuario)):
                    print ('Usuario ' + nombre + ' eliminado.')
                    raw_input()
                    return True
                else:
                    print ('No se pudo eliminar a ' + nombre + '.')
                    raw_input()
                    return False
            except:
                print ('No se pudo eliminar a ' + nombre + '.')
                raw_input()
                return False
        else:
            print ("Operacion cancelada")
            raw_input()

