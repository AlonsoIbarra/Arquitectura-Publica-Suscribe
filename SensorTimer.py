import random
import pika
import threading
import time


class SensorTimer():
    registros = []
    id = 0

    def __init__(self):
        self.set_data()

    def set_id(self):
        return random.randint(1000, 5000)

    def set_data(self):
        self.registros = [(1, 5, 'paracetamol'), (2, 7, 'Ibuprofeno')]

    def start_service(self):
        start_time = time.time()
        elapsed_time = 0
        while True:
            if(elapsed_time < int(time.time() - start_time)):
                elapsed_time = int(time.time() - start_time)
                threading.Thread(target=self.check, args=(elapsed_time,)).start()

    def check(self, time):
        for r in self.registros:
            if (int(time) % int(r[1])) == 0:
                connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
                channel = connection.channel()
                channel.exchange_declare(exchange='direct_medicamentos', type='direct')
                severity = 'medicamentos'
                mensaje = 'M:' + str(int(time)) + ':' + str(r[2])
                channel.basic_publish(exchange='direct_medicamentos', routing_key=severity, body=mensaje)
                print('+---------------+--------------------+-------------------------------+-------+')
                print('|      ' + str(int(time)) + '     |     ' + str(r[2]) + '     |      MEDICAMENTO ALERTA ENVIADA      |  ')
                print('+---------------+--------------------+-------------------------------+-------+')
                print('')
                connection.close()
