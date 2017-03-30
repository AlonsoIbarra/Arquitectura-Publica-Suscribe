import sys
from datos.Conexion import Conexion
from contexto.Usuario import Usuario


class ListaDeUsuarios():

    def __init__(self):
        pass

    def obtenerUsuarios(self):
        cn = Conexion()
        cn.abrir()
        usuarios = cn.ejecutaSELECT("select idUsuario, tipo, nombre, " +
                                    "contrasena from Usuarios")
        cn.cerrar()
        resultado = self.__mapearUsuarios(usuarios)
        return resultado

    def __mapearUsuarios(self, pUsuarios):
        lu = []
        for u in pUsuarios:
            usuario = Usuario()
            usuario.idUsuario = u[0]
            usuario.tipo = u[1]
            usuario.nombre = u[2]
            usuario.contrasena = u[3]
            lu.append(usuario)
        return lu

    def obtenerUsuarioPorNombre(self, nombreUsuario):
        cn = Conexion()
        cn.abrir()
        u = cn.ejecutaBusqueda("select idUsuario, tipo, nombre, " +
                               "contrasena from Usuarios where " +
                               "nombre = '" + nombreUsuario + "'")
        usuario = self.__devuelveUsuario(u)
        cn.cerrar()
        return usuario

    def __devuelveUsuario(self, pUsuario):
        usuario = Usuario()
        usuario.idUsuario = pUsuario[0]
        usuario.tipo = pUsuario[1]
        Usuario.nombre = pUsuario[2]
        Usuario.contrasena = pUsuario[3]
        return usuario

    def eliminarUsuario(self, nombreUsuario):
        cn = Conexion()
        cn.abrir()
        cn.ejecutaSQL("delete from Usuarios where nombre = '" + nombreUsuario +
                      "'")
        cn.cerrar()

    def agregarUsuario(self, pUsuario):
        cn = Conexion()
        cn.abrir()
        cn.ejecutaSQL("insert into Usuarios(tipo, nombre, " +
                      "contrasena) values(" + str(pUsuario.tipo) +
                      ", '" + pUsuario.nombre + "', '" +
                      pUsuario.contrasena + "')")
        cn.cerrar()
