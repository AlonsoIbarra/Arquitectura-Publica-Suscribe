#!/usr/bin/env python
# -*- coding: utf-8 -*-
# --------------------------------------------------------------------------------------------------
# Archivo: SignosVitales.py
# Capitulo: 3 Estilo Publica-Subscribe
# Autor(es): Perla Velasco & Yonathan Mtz.
# Version: 1.1 Agosto 2016
# Descripción:
#
#   Ésta clase define el rol de un monitor que muestra y notifica el resultado de los eventos
#   a los usuarios finales.
#
#   Las características de ésta clase son las siguientes:
#
#                                        SignosVitales.py
#           +-----------------------+-------------------------+------------------------+
#           |  Nombre del elemento  |     Responsabilidad     |      Propiedades       |
#           +-----------------------+-------------------------+------------------------+
#           |                       |                         |  - Es utilizado por    |
#           |                       |                         |    todas las clases    |
#           |                       |                         |    que reciben los     |
#           |        Monitor        |  - Mostrar datos a los  |    eventos.            |
#           |                       |    usuarios finales.    |  - Muestra el resulta- |
#           |                       |                         |    do de los eventos   |
#           |                       |                         |    un segundo después  |
#           |                       |                         |    de haber ocurrido.  |
#           +-----------------------+-------------------------+------------------------+
#
#   A continuación se describen los métodos que se implementaron en ésta clase:
#
#                                             Métodos:
#           +------------------------+--------------------------+-----------------------+
#           |         Nombre         |        Parámetros        |        Función        |
#           +------------------------+--------------------------+-----------------------+
#           |                        |                          |  - Imprime el mensa-  |
#           |   print_notification() |      String: message     |    je recibido desde  |
#           |                        |                          |    los subscriptores. |
#           +------------------------+--------------------------+-----------------------+
#
# --------------------------------------------------------------------------------------------------


class SignosVitales:

    def print_notification(self, message):
        print(str(message))
