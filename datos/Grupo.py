import sys
sys.path.append('/home/gustavo/Ejercicios_Python/MonitorConsola/Arquitectura-Publica-Suscribe')
from contexto.Miembro import Miembro
from contexto.Medicamento import Medicamento
from datos.Conexion import Conexion


class Grupo():
    idGrupo = 0
    periodo = 0
    medicamento = Medicamento()
    horaInicial = 0

    def __init__(self, pIdGrupo):
        cn = Conexion()
        cn.abrir()
        resultado = cn.ejecutaBusqueda("select idGrupo, periodo, " +
                                       "horaInicial, "
                                       "Medicamentos.idMedicamento, "
                                       "Medicamentos.descripcion " +
                                       "from Grupos inner join Medicamentos " +
                                       "on Grupos.idMedicamento = " +
                                       "Medicamentos.idMedicamento "
                                       "where idGrupo = " + str(pIdGrupo))

        cn.cerrar()
        self.__establecerPropiedades(resultado)

    def __establecerPropiedades(self, resultado):
        self.idGrupo = resultado[0]
        self.periodo = resultado[1]
        self.horaInicial = resultado[2]

        m = Medicamento()
        m.idMedicamento = resultado[3]
        m.descripcion = resultado[4]
        self.medicamento = m

    def agregarMiembro(self, pmiembro, pdosis):
        cn = Conexion()
        cn.abrir()
        cn.ejecutaSQL("insert into GrupoMiembros " +
                      "(idGrupo, idMiembro, dosis) " +
                      "values(" + str(self.idGrupo) + ", " +
                      str(pmiembro.idMiembro) + ", " +
                      str(pdosis) + ")")
        cn.cerrar()

    def obtenerMiembros(self):
        cn = Conexion()
        cn.abrir()
        resultado = cn.ejecutaSELECT("select dosis, " +
                                     "Miembros.idMiembro, " +
                                     "Miembros.nombres, " +
                                     "Miembros.apellidos, " +
                                     "Miembros.edad, " +
                                     "Miembros.IDsTemperatura, " +
                                     "Miembros.IDsAcelerometro, " +
                                     "Miembros.IDsRitmoCardiaco, " +
                                     "Miembros.IDsPresion " +
                                     "from (Grupos inner join GrupoMiembros " +
                                     "on Grupos.idGrupo = " +
                                     "GrupoMiembros.idGrupo) inner join " +
                                     "Miembros on GrupoMiembros.idMiembro " +
                                     "= Miembros.idMiembro Where " +
                                     "Grupos.idGrupo = " + str(self.idGrupo))
        cn.cerrar()
        return self.__mapearMiembrosenLista(resultado)

    def __mapearMiembrosenLista(self, resultado):
        ListaDeMiembros = []
        dosis = 0
        for r in resultado:
            dosis = r[0]
            u = Miembro()
            u.idMiembro = r[1]
            u.nombres = r[2]
            u.apellidos = r[3]
            u.edad = r[4]
            u.IDsTemperatura = r[5]
            u.IDsAcelerometro = r[6]
            u.IDsRitmoCardiaco = r[7]
            u.IDsPresion = r[8]

            ListaDeMiembros.append((u, dosis))

        return ListaDeMiembros
