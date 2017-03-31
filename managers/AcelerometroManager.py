#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pika
import sys
from SignosVitales import SignosVitales



class AcelerometroManager:
    posicion_maximo = 0.0
    values_parameters = []

    def start_consuming(self):
        try:
            ip = sys.argv[1]
            usuario = sys.argv[2]
            contrasena = sys.argv[3]
            credentials = pika.PlainCredentials(usuario, contrasena)
            parameters = pika.ConnectionParameters(ip, 5672, '/',credentials)
            connection = pika.BlockingConnection(parameters)
        except:
            connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        channel = connection.channel()
        channel.exchange_declare(exchange='direct_rhythm', type='direct')
        result = channel.queue_declare(exclusive=True)
        queue_name = result.method.queue
        severity = 'acelerometro'
        channel.queue_bind(exchange='direct_acelerometro', queue=queue_name, routing_key=severity)
        print(' [*] Inicio de monitoreo de acelerometro. Presiona CTRL+C para finalizar monitoreo')
        channel.basic_consume(self.callback,
                              queue=queue_name,
                              no_ack=True)
        channel.start_consuming()

    def callback(self, ch, method, properties, body):
        values = body.split(':')
        try:
            componenteX = values[4].split(',')[0]
        #    componenteY = values[5].split(',')[0]
        #    componenteZ = values[6].split(',')[0]
        #    if (-0.150 <= float(componenteX) <= float(0.5)) and (-0.150 <= float(componenteY) <= 0.999) and (-0.999 <= float(componenteZ) <= 0.99):
            #if (-0.150 <= float(componenteX) <= float(0.5)):
            monitor = SignosVitales()
            monitor.print_notification('+----------+-----------------------+')
            monitor.print_notification('|   ' + str(values[1]) + '   |   SE CALLÓ   |  ' + str(values[2]) + '  |')
            monitor.print_notification('+----------+-----------------------+')
            monitor.print_notification('')
            monitor.print_notification('')
        except:
            pass


test = AcelerometroManager()
test.start_consuming()
