from datos.Grupo import Grupo
from datos.ListaDeGrupos import ListaDeGrupos
import threading
import time

class TimerMedicamento():
    def __init__(self):
        pass

    def start_timer(self):
            start_time = time.time()
            elapsed_time = 0
            while True:
                if(elapsed_time < int(time.time() - start_time)):
                    elapsed_time = int(time.time() - start_time)
                    print elapsed_time
                    threading.Thread(target=self.check, args=(elapsed_time,)).start()
    def construir_mensaje(self, grupo):
        mensaje = ''
        mensaje += '+---------------------------------------------+\n'
        mensaje += '|             Alerta de Medicamento           |\n'
        mensaje += '+---------------------------------------------+\n'
        mensaje += 'Medicamento: '+ str(grupo.medicamento.descripcion)+'\n'
        mensaje += '+---------------------------------------------+\n'
        mensaje += '\tUsuarios:\t\t\tDosis:\n'
        mensaje += '\n'
        for usuario in grupo.obtenerUsuarios():
            mensaje += '\t'+usuario[0].nombres+' '+usuario[0].apellidos 
            mensaje += '\t\t\t'+str(usuario[1])+'\n'
        print mensaje



    def check(self, time):
        listagrupo = ListaDeGrupos()
        for r in listagrupo.obtenerGrupos():
            if (int(time) % int(r[1])) == 0:
                grupo = Grupo(r[0])
                self.construir_mensaje(grupo)
