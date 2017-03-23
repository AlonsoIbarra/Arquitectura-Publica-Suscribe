#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
import pika


class SensorAcelerometro():
    nombre = None
    id = 0

    def __init__(self, nombre):
        self.nombre = nombre
        self.id = int(self.set_id())

    def set_id(self):
        return random.randint(1000, 5000)

    def get_name(self):
        return self.nombre

    def start_service(self):
        connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        channel = connection.channel()
        channel.exchange_declare(exchange='direct_acelerometro', type='direct')
        severity = 'acelerometro'
        componenteX = self.simulate_data()
        componenteY = self.simulate_data()
        componenteZ = self.simulate_data()
        mensaje = 'AC:' + str(self.id) + ':' + self.nombre + ':[x:' + str(componenteX) + ', y:' + str(componenteY) + ', z:' + str(componenteZ) + ']'
        channel.basic_publish(exchange='direct_acelerometro',
                              routing_key=severity, body=mensaje)
        print('+---------------+--------------------+-------------------------------+-------+')
        print('|      ' + str(self.id) + '     |     ' + self.nombre + '     |      ACELEROMETRO ENVIADO      |  [x:' + str(componenteX) + ', y:' + str(componenteY) + ', z:' + str(componenteZ) + ']  |')
        print('+---------------+--------------------+-------------------------------+-------+')
        print('')
        connection.close()

    def simulate_data(self):
        return random.uniform(-1, 1)
