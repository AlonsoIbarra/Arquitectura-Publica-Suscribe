# Capitulo 3

# "Health Monitoring Simulator"

# ##Prerequisitos

# Antes de ejecutar el código aseguradte de haber realizado las acciones indicadas en la Wiki -> HealthMonitoringSimulator
# [Prerequisitos](https://github.com/AlonsoIbarra/Arquitectura-Publica-Suscribe/wiki)
# ##Ejecutar Simulador
# Para ejecutar el simulador es necesario seguir los sigiuentes pasos:
# 1. Abrir terminal en Ubuntu / Fedora.
# 2. Clonar el repositorio:   `git clone https://github.com/AlexMtz/Estilos-De-Arquitectura-De-Software.git`
# 3. Ingresar a la carpeta que descargamos:   `cd Estilos-De-Arquitectura-De-Software/`
# 4. Acceder al capítulo 3:  `cd capitulo_3/`
# 5. Ejecutar el simulador: `python Simulador.py`

# Si el simulador se ejecuto de manera correcta encontraremos lo siguiente:
# [Simulador.py](https://drive.google.com/open?id=0B1FMJsKfgRaPVTZPOWVDWks2eGc)


# Agregar Usuarios a RabbitMQ

1.- Activa el Plugin de administración de RabbitMQ

La ruta depende de la versión de RabbitMQ que tengas.
cd /usr/lib/rabbitmq/lib/rabbitmq_server-3.5.7/sbin
Activa el plugin
# sudo rabbitmq-plugins enable rabbitmq_management

2.- Reinicia el servidor RabbitMQ

# sudo rabbitmqctl stop

# sudo rabbitmq-server -detached
Warning: PID file not written; -detached was passed.

3.- Accede al dashboard de RabbitMQ

desde tu browser accede a http://{tu-direccion.ip}:15672/

4.- Crea una nueva cuenta RabbitMQ

Haz click en la pestaña Admin, llena los datos de usuario, password y tag.
Haz click en "add User"

5.-Configura permisos a las cuenta de Usuario.
Haz click en la pestaña Admin, Haz click en el nombre de tu usuario.
Usa los valores predeterminados y haz click en "Set Permission"


