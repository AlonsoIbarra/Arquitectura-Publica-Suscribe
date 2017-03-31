#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from contexto.Grupo import Grupo as GrupoElemento
from datos.ListaDeGrupos import ListaDeGrupos
from datos.ListaDeMedicamentos import ListaDeMedicamentos
from contexto.Medicamento import Medicamento


class VistaGrupos():

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
        if periodo == -1:
        	return False
        horaInicial = self.readInt('Ingrese hora inicial en valo entero, en formato de 24 horas. ')
        if horaInicial == -1:
        	return False
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

    def readInt(self, msg):
        try:
            return int(raw_input(msg))
        except ValueError:
            print "ERROR: Valor no numerico entero..."
            raw_input('')
            return -1

    def listarMedicamentos(self, lm):
        print('+---------------------------------------------+')
        print('|  ID  |  MEDICAMENTO                        |')
        print('+---------------------------------------------+')
        for m in lm.obtenerMedicamentos():
            print('|  ' + str(m[0]) + '  |  ' + str(m[1]) + '       |')
            print('+---------------------------------------------+')
        raw_input()
