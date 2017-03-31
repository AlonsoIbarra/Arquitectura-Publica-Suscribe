#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import getpass
import hashlib
from contexto.Usuario import Usuario
from datos.ListaDeUsuarios import ListaDeUsuarios


class VistaUsuarios():

    def menuUsuarios(self):
        lu = ListaDeUsuarios()
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
            print('|  3.-  LISTAR USUARIOS                       |')
            print('+---------------------------------------------+')
            print('|  6.-  REGRESAR                              |')
            print('+---------------------------------------------+')
            op = self.readInt("Ingrese opción: ")

            if op == 1:
                self.agregarUsuario(lu)
            elif op == 2:
                self.eliminarUsuario(lu)
            elif op == 3:
                self.listarUsuarios(lu)
            elif op == 6:
                print "regresando..."
                break
            else:
                pass

    def listarUsuarios(self, lu):
        os.system('clear')
        print('+---------------------------------------------+')
        print('|  TIPO  |  NOMBRE                            |')
        for u in lu.obtenerUsuarios():
            print('+---------------------------------------------+')
            print ('|  ' + str(u.tipo) + '  |  ' + u.nombre + '|')
        print('+---------------------------------------------+')
        raw_input()
        return True

    def agregarUsuario(self, lu):
        os.system('clear')
        nombre = raw_input('Ingresa el nombre del usuario: ')
        try:
            usuario = lu.obtenerUsuarioPorNombre(nombre)
        except:
            usuario = None
        if isinstance(usuario, Usuario):
            print ('El usuario ya esta registrado.')
            raw_input()
            if str(raw_input('Deseas registrar otro usuario? s/n  ')) == str('s'):
                return self.agregarUsuario(lu)
            else:
                return False
        else:
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

    def eliminarUsuario(self, lu):
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
            return False

    def readInt(self, msg):
        try:
            return int(raw_input(msg))
        except ValueError:
            print "ERROR: Valor no numerico entero..."
            raw_input('')
            return -1
