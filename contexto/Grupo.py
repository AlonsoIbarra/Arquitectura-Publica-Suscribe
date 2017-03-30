import sys
sys.path.append('/home/gustavo/Ejercicios_Python/MonitorConsola/Arquitectura-Publica-Suscribe')
from contexto.Medicamento import Medicamento
from contexto.Miembro import Miembro

class Grupo():
    idGrupo = 0
    periodo = 0
    medicamento = Medicamento()
    horaInicial = 0
    listaDeMiembros = []

    def __init__(self):
        pass
