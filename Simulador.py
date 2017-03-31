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
from contexto.Grupo import Grupo as GrupoElemento
from datos.ListaDeGrupos import ListaDeGrupos
from contexto.Usuario import Usuario
from datos.ListaDeUsuarios import ListaDeUsuarios
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
        #self.login()
        self.menuAdministrador()
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
            print('|  2.-  GESTIÓN DE MIEMBROS                   |')
            print('+---------------------------------------------+')
            print('|  3.-  GESTIÓN DE GRUPOS                     |')
            print('+---------------------------------------------+')
            print('|  4.-  GESTIÓN DE MEDICAMENTOS               |')
            print('+---------------------------------------------+')
            print('|  5.-  GESTIÓN DE SIGNOS VITALES             |')
            print('+---------------------------------------------+')
            print('|  6.-  INICIAR SIMULACIÓN                    |')
            print('+---------------------------------------------+')
            print('|  7.-  SALIR DE SIMULADOR                    |')
            print('+---------------------------------------------+')
            op = self.readInt("Ingrese opción: ")
            if op == 1:
                self.menuUsuarios()
            elif op == 2:
                self.menuMiembros()
            elif op == 3:
                self.menuGrupos()
            elif op == 4:
                self.menuMedicamentos()
            elif op == 5:
                self.menuSignosVitales()
            elif op == 6:
                print "iniciando simulación..."
                self.iniciarSimulacion()
            elif op == 7:
                print "saliendo..."
                os.system('clear')
                break
            else:
                pass

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

    def menuGrupos(self):
        lg = ListaDeGrupos()
        while True:
            os.system('clear')
            print('')
            print('+---------------------------------------------+')
            print('|                 MENÚ GRUPOS                 |')
            print('+---------------------------------------------+')
            print('|  1.-  AGRAGAR GRUPO                         |')
            print('+---------------------------------------------+')
            print('|  2.-  ELIMIAR GRUPO                         |')
            print('+---------------------------------------------+')
            print('|  3.-  LISTAR GRUPOS                         |')
            print('+---------------------------------------------+')
            print('|  6.-  REGRESAR                              |')
            print('+---------------------------------------------+')
            op = self.readInt("Ingrese opción: ")
            if op == 1:
                self.agregarGrupo(lg)
            elif op == 2:
                self.eliminarGrupo(lg)
            elif op == 3:
                self.listarGrupos(lg)
            elif op == 6:
                print "regresando..."
                break
            else:
                pass

    def __leerMedicamento(self):
        lm = ListaDeMedicamentos()
        self.listarMedicamentos(lm)
        idMedicamento = self.readInt('Ingrese el id del medicamento a asociar. ')
        try:
            medicamento = lm.obtenerMedicamentoPorId(idMedicamento)
            if(raw_input('Desea agregar ' + medicamento.descripcion + '? s/n ')) == str('s'):
                return medicamento
            else:
                if(raw_input('Desea continuar buscando? s/n ')) == str('s'):
                    return self.__leerMedicamento()
                else:
                    print("Cancelando operación")
                    raw_input()
                    return -1
        except:
            print ('No se encontro el registro, intente nuevamente.')
            raw_input()
            return self.__leerMedicamento()

    def agregarGrupo(self, lg):
        periodo = self.readInt('Ingrese periodo de tiempo en un valor entero. ')
        horaInicial = self.readInt('Ingrese hora inicial en valo entero, en formato de 24 horas. ')
        medicamento = self.__leerMedicamento()
        if medicamento != -1:
            grupo = GrupoElemento()
            grupo.periodo = periodo
            grupo.medicamento = medicamento
            grupo.horaInicial = horaInicial
            lg.crearGrupo(grupo)
            print ("Se creo el grupo exitosamente")
            raw_input()
            return True
        else:
            print ("Ocurrio un error intente nuevamente.")
            raw_input()
            return False

    def eliminarGrupo(self, lg):
        idGrupo = self.readInt('Ingrese id de grupo ')
        try:
            grupo = lg.obtenerGrupoPorId(idGrupo)
        except:
            print ('Grupo no encontrado.')
            raw_input()
            return False
        if (raw_input('Confirma eliminar el grupo número ' + str(idGrupo) + '? s/n ')) == str('s'):
            lg.eliminarGrupo(grupo)
            print ('Grupo eliminado exitosamente.')
            raw_input()
            return True
        else:
            print ('Operación cancelada.')
            raw_input()
            return False

    def listarGrupos(self, lg):
        lm = ListaDeMedicamentos()
        lst = lg.obtenerGrupos()
        print('+-------------------------------------------------+')
        print('|  ID  |  PERIODO  | MEDICAMENTO  | HORA INICIAL  |')
        for g in lst:
            try:
                medicamento = lm.obtenerMedicamentoPorId(int(g[2]))
            except:
                medicamento = Medicamento()
                medicamento.descripcion = "Desconocido"
            print('+---------------------------------------------+')
            print('|  ' + str(g[0]) + '  |  ' + str(g[1]) + '       | ' + medicamento.descripcion + '  | ' + str(g[3]) + '  |')
        raw_input()
        return True

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
        print('+        ' + str(signo.max) + '           |         ' + str(signo.max) + '         |')
        print('+---------------------------------------------+')
        max = self.readInt("Ingrese máximo: ")
        min = self.readInt("Ingrese mínimo: ")
        signo.max = max
        signo.min = min
        if (ls.actualizarSigno(signo)):
            print ('Valores de temperatura actualizos correctamente.')
            return True
        else:
            print ('Valores de temperatura no actualizos.')
            return True

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
