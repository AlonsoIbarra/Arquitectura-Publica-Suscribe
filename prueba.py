
from contexto.Miembro import Miembro
from datos.ListaDeMiembros import ListaDeMiembros
from contexto.Medicamento import Medicamento
from datos.ListaDeMedicamentos import ListaDeMedicamentos
from datos.ListaDeGrupos import ListaDeGrupos
from contexto.Grupo import Grupo
from datos.Grupo import Grupo as Group
from datos.ListaDeMiembros import ListaDeMiembros as LDU

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
g.agregarMiembro(u, 200)

# devuelve los miembros del grupo
miembros = g.obtenerMiembros()

for m in miembros:
    u = m[0]
    dosis = m[1]
    print(u.nombres + ", " + u.apellidos + " dosis: " + str(dosis))
