import sys
sys.path.append('/home/gustavo/Ejercicios_Python/MonitorConsola/Arquitectura-Publica-Suscribe')
from contexto.Miembro import Miembro
from datos.Conexion import Conexion


class ListaDeMiembros():
    def __init__(self):
        pass

    def agregarMiembro(self, pmiembro):
        cn = Conexion()
        cn.abrir()
        cn.ejecutaSQL("INSERT INTO Miembros (nombres, apellidos, edad, " +
                      "IDsTemperatura, IDsAcelerometro, IDsRitmoCardiaco, " +
                      "IDsPresion) VALUES ('" + pmiembro.nombres + "', '" +
                      pmiembro.apellidos + "', " +
                      str(pmiembro.edad) + ", " +
                      str(pmiembro.IDsTemperatura) + ", " +
                      str(pmiembro.IDsAcelerometro) + ", " +
                      str(pmiembro.IDsRitmoCardiaco) + ", " +
                      str(pmiembro.IDsPresion) + ")")
        cn.cerrar()

    def obtenerMiembros(self):
        cn = Conexion()
        cn.abrir()
        resultado = cn.ejecutaSELECT("SELECT * FROM Miembros")
        cn.cerrar()

        return self.__mapearMiembrosenLista(resultado)

    def obtenerMiembroPorId(self, idMiembro):
        cn = Conexion()
        cn.abrir()
        miembro = cn.ejecutaBusqueda("select idMiembro, nombres, " +
                                     "apellidos, edad, " +
                                     "IDsTemperatura, IDsAcelerometro, " +
                                     "IDsRitmoCardiaco, IDsPresion " +
                                     "from Miembros where idMiembro = " +
                                     str(idMiembro))

        cn.cerrar()
        return self.__mapearEnMiembro(miembro)

    def __mapearEnMiembro(self, pMiembro):
        u = Miembro()
        u.idMiembro = pMiembro[0]
        u.nombres = pMiembro[1]
        u.apellidos = pMiembro[2]
        u.edad = pMiembro[3]
        u.IDsTemperatura = pMiembro[4]
        u.IDsAcelerometro = pMiembro[5]
        u.IDsRitmoCardiaco = pMiembro[6]
        u.IDsPresion = pMiembro[7]

        return u

    def __mapearMiembrosenLista(self, resultado):
        ListaDeMiembros = []
        for r in resultado:
            u = Miembro()
            u.idMiembro = r[0]
            u.nombres = r[1]
            u.apellidos = r[2]
            u.edad = r[3]
            u.IDsTemperatura = r[4]
            u.IDsAcelerometro = r[5]
            u.IDsRitmoCardiaco = r[6]
            u.IDsPresion = r[7]

            ListaDeMiembros.append(u)

        return ListaDeMiembros
