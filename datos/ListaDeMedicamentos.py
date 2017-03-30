import sys
sys.path.append('/home/gustavo/Ejercicios_Python/MonitorConsola/Arquitectura-Publica-Suscribe')
from contexto.Medicamento import Medicamento
from datos.Conexion import Conexion


class ListaDeMedicamentos():
    def __init__(self):
        pass

    def agregarMedicamento(self, medicamento):
        cn = Conexion()
        cn.abrir()
        cn.ejecutaSQL("insert into Medicamentos (descripcion) values ('" +
                      medicamento.descripcion + "')")
        cn.cerrar()

    def eliminarMedicamento(self, medicamento):
        cn = Conexion()
        cn.abrir()
        cn.ejecutaSQL("delete from Medicamentos  where idMedicamento =" + str(m.idMedicamento) + "")
        cn.cerrar()
        return True

    def obtenerMedicamentos(self):
        cn = Conexion()
        cn.abrir()
        resultado = cn.ejecutaSELECT("select * from Medicamentos")

        cn.cerrar()
        return resultado

    def obtenerMedicamentoPorId(self, idMedicamento):
        cn = Conexion()
        cn.abrir()
        resultado = cn.ejecutaBusqueda("select * from Medicamentos " +
                                       "where idMedicamento = " +
                                       str(idMedicamento))

        medicamento = self.__mapearMedicamento(resultado)

        cn.cerrar()
        return medicamento

    def __mapearMedicamento(self, presultado):
        m = Medicamento()
        m.idMedicamento = presultado[0]
        m.descripcion = presultado[1]
        return m
