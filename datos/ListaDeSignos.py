import sys
from datos.Conexion import Conexion
from contexto.Signo import Signo


class ListaDeSignos():

    def __init__(self):
        pass

    def obtenerSignoPorDescripcion(self, pDescripcion):
        cn = Conexion()
        cn.abrir()
        s = cn.ejecutaBusqueda("select idSigno, descripcion, min, max " +
                               "from SignosVitales where descripcion = '" +
                               pDescripcion + "'")
        cn.cerrar()
        signo = self.__mapearSigno(s)
        return signo

    def __mapearSigno(self, pSigno):
        signo = Signo()
        signo.idSigno = pSigno[0]
        signo.descripcion = pSigno[1]
        signo.min = pSigno[2]
        signo.max = pSigno[3]
        return signo

    def agregarSigno(self, pSigno):
        cn = Conexion()
        cn.abrir()
        cn.ejecutaSQL("insert into SignosVitales(descripcion, min, " +
                      "max) values ('" + pSigno.descripcion + "', " +
                      str(pSigno.min) + ", " + str(pSigno.max) + ")")
        cn.cerrar()

    def obtenerSignos(self):
        cn = Conexion()
        cn.abrir()
        signos = cn.ejecutaSELECT("select idSigno, descripcion, min, max " +
                                  "from SignosVitales")

        cn.cerrar()
        resultado = self.__mapearSignos(signos)
        return resultado

    def __mapearSignos(self, pSignos):
        signos = []
        for s in pSignos:
            signo = Signo()
            signo.idSigno = s[0]
            signo.descripcion = s[1]
            signo.min = s[2]
            signo.max = s[3]
            signos.append(signo)
        return signos
