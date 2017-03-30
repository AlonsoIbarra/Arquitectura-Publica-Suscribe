
from contexto.Miembro import Miembro
from datos.ListaDeMiembros import ListaDeMiembros
from contexto.Medicamento import Medicamento
from datos.ListaDeMedicamentos import ListaDeMedicamentos
from datos.ListaDeGrupos import ListaDeGrupos
from contexto.Grupo import Grupo
from datos.Grupo import Grupo as Group
from datos.ListaDeMiembros import ListaDeMiembros as LDU
from datos.ListaDeUsuarios import ListaDeUsuarios
from contexto.Usuario import Usuario
from contexto.Signo import Signo
from datos.ListaDeSignos import ListaDeSignos

# Agregar Usuario
u = Miembro()
u.nombres = "Josue"
u.apellidos = "lopez"
u.edad = 37
u.IDsTemperatura = 1
u.IDsPresion = 1
u.IDsAcelerometro = 1
u.IDsRitmoCardiaco = 1

l = ListaDeMiembros()
l.agregarMiembro(u)

# Obtener lista de usuarios
miembros = l.obtenerMiembros()

# Busca usuario por id
u = l.obtenerMiembroPorId(1)


# agregar Medicamento
m = Medicamento()
m.descripcion = "Yodohidroxiquinoleina"
l = ListaDeMedicamentos()
l.agregarMedicamento(m)

# devuelve medicamento
medicamentos = l.obtenerMedicamentos()

# obtenerMedicamentoPorId
m = l.obtenerMedicamentoPorId(1)


# agregar grupos
g = Grupo()
g.periodo = 4
g.medicamento = m
g.horaInicial = 12

lg = ListaDeGrupos()
lg.crearGrupo(g)

# lista de todos los grupos
listaDeGrupos = lg.obtenerGrupos()


l = LDU()
u = l.obtenerMiembroPorId(1)


g = Group(21)
# agrega miembro al grupo y dosis
# g.agregarMiembro(u, 200)

# devuelve los miembros del grupo
miembros = g.obtenerMiembros()

for m in miembros:
    u = m[0]
    dosis = m[1]
    print(u.nombres + ", " + u.apellidos + " dosis: " + str(dosis))


lu = ListaDeUsuarios()

u = Usuario()
u.tipo = 1
u.nombre = "luis"
u.contrasena = "luis"

# lu.agregarUsuario(u)

u = lu.obtenerUsuarioPorNombre("saul")

print(u.nombre + ": " + u.contrasena)

# lu.eliminarUsuario("miles")


users = lu.obtenerUsuarios()
for u in users:
    print(u.nombre)

s = Signo()
"""
s.descripcion = "Presion"
s.min = 10
s.max = 100
ls = ListaDeSignos()
ls.agregarSigno(s)

s = Signo()
s.descripcion = "Temperatura"
s.min = 35
s.max = 37
"""
ls = ListaDeSignos()
#ls.agregarSigno(s)

s1 = ls.obtenerSignoPorDescripcion("Presion")
print(s1.descripcion + " : max" + str(s1.max))
ss = ls.obtenerSignos()

for s in ss:
    print(s.descripcion)
