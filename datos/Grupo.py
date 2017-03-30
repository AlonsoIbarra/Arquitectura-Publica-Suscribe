import sys
sys.path.append('/home/gustavo/Ejercicios_Python/MonitorConsola/Arquitectura-Publica-Suscribe')
from contexto.Usuario import Usuario
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

    def agregarUsuario(self, usuario, pdosis):
        cn = Conexion()
        cn.abrir()
        cn.ejecutaSQL("insert into GrupoUsuarios " +
                      "(idGrupo, idUsuario, dosis) " +
                      "values(" + str(self.idGrupo) + ", " +
                      str(usuario.idUsuario) + ", " +
                      str(pdosis) + ")")
        cn.cerrar()

    def obtenerUsuarios(self):
        cn = Conexion()
        cn.abrir()
        resultado = cn.ejecutaSELECT("select dosis, " +
                                     "Usuarios.idUsuario, " +
                                     "Usuarios.nombres, " +
                                     "Usuarios.apellidos, " +
                                     "Usuarios.edad, " +
                                     "Usuarios.IDsTemperatura, " +
                                     "Usuarios.IDsAcelerometro, " +
                                     "Usuarios.IDsRitmoCardiaco, " +
                                     "Usuarios.IDsPresion " +
                                     "from (Grupos inner join GrupoUsuarios " +
                                     "on Grupos.idGrupo = " +
                                     "GrupoUsuarios.idGrupo) inner join " +
                                     "Usuarios on GrupoUsuarios.idUsuario " +
                                     "= Usuarios.idUsuario " +
                                     "where Grupos.idGrupo="+ str(self.idGrupo))

        cn.cerrar()
        return self.__mapearUsuariosenLista(resultado)

    def __mapearUsuariosenLista(self, resultado):
        ListaDeUsuarios = []
        dosis = 0
        for r in resultado:
            dosis = r[0]
            u = Usuario()
            u.idUsuario = r[1]
            u.nombres = r[2]
            u.apellidos = r[3]
            u.edad = r[4]
            u.IDsTemperatura = r[5]
            u.IDsAcelerometro = r[6]
            u.IDsRitmoCardiaco = r[7]
            u.IDsPresion = r[8]

            ListaDeUsuarios.append((u, dosis))

        return ListaDeUsuarios
