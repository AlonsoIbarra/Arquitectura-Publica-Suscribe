#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from contexto.Medicamento import Medicamento
from datos.ListaDeMedicamentos import ListaDeMedicamentos

class VistaMedicamentos():

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

    def readInt(self, msg):
        try:
            return int(raw_input(msg))
        except ValueError:
            print "ERROR: Valor no numerico entero..."
            raw_input('')
            return -1
