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

    def eliminarGrupo(self, grupo):
        cn = Conexion()
        cn.abrir()
        cn.ejecutaSQL("delete from Grupos  where idGrupo =" + str(grupo.idGrupo) + "")
        cn.cerrar()
        return True

    def obtenerGrupos(self):
        con = Conexion()
        con.abrir()
        grupos = con.ejecutaSELECT("select * from Grupos")
        con.cerrar()
        return grupos

    def obtenerGrupoPorId(self, idGrupo):
        cn = Conexion()
        cn.abrir()
        resultado = cn.ejecutaBusqueda("select * from Grupos " +
                                       "where idGrupo = " +
                                       str(idGrupo))
        grupo = self.__mapearGrupo(resultado)
        cn.cerrar()
        return grupo

    def __mapearGrupo(self, presultado):
        m = Grupo()
        m.idGrupo = presultado[0]
        m.periodo = presultado[1]
        m.idMedicamento = presultado[2]
        m.horaInicial = presultado[3]
        return m
