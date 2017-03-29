# from contexto.Usuario import Usuario
# from datos.ListaDeUsuarios import ListaDeUsuarios

# u = Usuario()
# u.nombres="angel"
# u.apellidos="lazaro"
# u.edad=37
# u.IDsTemperatura=1
# u.IDsPresion=1
# u.IDsAcelerometro=1
# u.IDsRitmoCardiaco=1

# l = ListaDeUsuarios()
# l.agregarUsuario(u)

# print(l.obtenerUsuarios())

from contexto.Medicamento import Medicamento
from datos.ListaDeGrupos import ListaDeGrupos
from datos.ListaDeMedicamentos import ListaDeMedicamentos
from contexto.Grupo import Grupo
from datos.ListaDeUsuarios import ListaDeUsuarios

# m = Medicamento()
# m.descripcion = "Cloranfenamida"

l = ListaDeMedicamentos()
m = l.obtenerMedicamentoPorId(1)

g = Grupo()
g.periodo = 4
g.medicamento = m
g.horaInicial = 12



lg = ListaDeGrupos()
lg.crearGrupo(g)

# print(lg.obtenerGrupos())

l = ListaDeUsuarios()
u = l.obtenerUsuarioPorId(1)
print(u.nombres)
# l.agregarMedicamento(m)

# print(l.obtenerMedicamentos())
