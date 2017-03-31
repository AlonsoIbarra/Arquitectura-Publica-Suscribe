import sys
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
        return True

    def agregarMiembroGrupo(self, idMiembro, idGrupo, dosis):
        cn = Conexion()
        cn.abrir()
        cn.ejecutaSQL("INSERT INTO GrupoMiembros (idGrupo,idMiembro,dosis) " +
                      "VALUES ('" + str(idGrupo) + "','" + str(idMiembro) + "','" + dosis + "')")
        cn.cerrar()
        return True

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

    def obtenerMiembroGrupo(self):
        cn = Conexion()
        cn.abrir()
        resultado = cn.ejecutaSELECT("SELECT g.idGrupo, m.nombres || ' ' || m.apellidos as nombre,me.descripcion, dosis " +
                                        "FROM GrupoMiembros gm " +
                                        "inner join Miembros m on m.idMiembro=gm.idMiembro " +
                                        "inner join Grupos g on g.idGrupo=gm.idGrupo " +
                                        "inner join Medicamentos me on me.idMedicamento=g.idMedicamento order by g.idGrupo")

        cn.cerrar()
        return resultado

    def eliminarMiembro(self, pMiembro):
        cn = Conexion()
        cn.abrir()

        cn.ejecutaSQL("delete from Miembros  where idMiembro = " +
                      str(pMiembro.idMiembro) + "")

        cn.cerrar()
        return True

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

