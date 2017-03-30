import sys
sys.path.append('/home/gustavo/Ejercicios_Python/MonitorConsola/Arquitectura-Publica-Suscribe')
from contexto.Usuario import Usuario
from datos.Conexion import Conexion


class ListaDeUsuarios():
    def __init__(self):
        pass

    def agregarUsuario(self, usuario):
        cn = Conexion()
        cn.abrir()
        cn.ejecutaSQL("INSERT INTO Usuarios (nombres, apellidos, edad, " +
                      "IDsTemperatura, IDsAcelerometro, IDsRitmoCardiaco, " +
                      "IDsPresion) VALUES ('" + usuario.nombres + "', '" +
                      usuario.apellidos + "', " +
                      str(usuario.edad) + ", " +
                      str(usuario.IDsTemperatura) + ", " +
                      str(usuario.IDsAcelerometro) + ", " +
                      str(usuario.IDsRitmoCardiaco) + ", " +
                      str(usuario.IDsPresion) + ")")
        cn.cerrar()

    def obtenerUsuarios(self):
        cn = Conexion()
        cn.abrir()
        resultado = cn.ejecutaSELECT("SELECT * FROM Usuarios")
        cn.cerrar()

        return self.__mapearUsuariosenLista(resultado)

    def obtenerUsuarioPorId(self, idUsuario):
        cn = Conexion()
        cn.abrir()
        usuario = cn.ejecutaBusqueda("select idUsuario, nombres, " +
                                     "apellidos, edad, " +
                                     "IDsTemperatura, IDsAcelerometro, " +
                                     "IDsRitmoCardiaco, IDsPresion " +
                                     "from Usuarios where idUsuario = " +
                                     str(idUsuario))

        cn.cerrar()
        return self.__mapearEnUsuario(usuario)

    def __mapearEnUsuario(self, pUsuario):
        u = Usuario()
        u.idUsuario = pUsuario[0]
        u.nombres = pUsuario[1]
        u.apellidos = pUsuario[2]
        u.edad = pUsuario[3]
        u.IDsTemperatura = pUsuario[4]
        u.IDsAcelerometro = pUsuario[5]
        u.IDsRitmoCardiaco = pUsuario[6]
        u.IDsPresion = pUsuario[7]

        return u

    def __mapearUsuariosenLista(self, resultado):
        ListaDeUsuarios = []
        for r in resultado:
            u = Usuario()
            u.idUsuario = r[0]
            u.nombres = r[1]
            u.apellidos = r[2]
            u.edad = r[3]
            u.IDsTemperatura = r[4]
            u.IDsAcelerometro = r[5]
            u.IDsRitmoCardiaco = r[6]
            u.IDsPresion = r[7]

            ListaDeUsuarios.append(u)

        return ListaDeUsuarios
