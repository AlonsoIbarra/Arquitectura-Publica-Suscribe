import sys
sys.path.append('/home/gustavo/Ejercicios_Python/MonitorConsola/Arquitectura-Publica-Suscribe')
from datos.Conexion import Conexion
from contexto.Grupo import Grupo


class ListaDeGrupos():
    def __init__(self):
        pass

    def crearGrupo(self, grupo):
        con = Conexion()
        con.abrir()
        con.ejecutaSQL("insert into Grupos(periodo, horaInicial, " +
                       "idMedicamento) values(" +
                       str(grupo.periodo) + ", " +
                       str(grupo.horaInicial) + ", " +
                       str(grupo.medicamento.idMedicamento) + ")")
        con.cerrar()

    def obtenerGrupos(self):
        con = Conexion()
        con.abrir()
        grupos = con.ejecutaSELECT("select * from Grupos")
        con.cerrar()
        return grupos
