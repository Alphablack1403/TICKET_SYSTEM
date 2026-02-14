##Ticket System - Django

    Mini sistema de gestión de tickets desarrollado en Django como prueba técnica. Permite crear, listar, actualizar estado y prioridad, así como gestionar comentarios asociados a cada ticket, persistiendo la información en base de datos SQL (SQLite).

##Tecnologías utilizadas

    Python 3.10+

    Django

    SQLite

    HTML / CSS (plantillas Django)

##Requisitos

    Python 3.10 o superior

    pip

    Git

##Instalación y ejecución en local
    1️⃣ Clonar el repositorio
    git clone <URL_DEL_REPOSITORIO>
    cd ticket_system

    2️⃣ Crear entorno virtual
    python -m venv venv

    3️⃣ Activar entorno virtual

    Windows:

    venv\Scripts\activate


    Linux / Mac:

    source venv/bin/activate

    4️⃣ Instalar dependencias
    pip install -r requirements.txt

    5️⃣ Aplicar migraciones
    python manage.py migrate

    6️⃣ Crear superusuario (opcional, recomendado)
    python manage.py createsuperuser

    7️⃣ Ejecutar el servidor
    python manage.py runserver


    La aplicación estará disponible en:
    http://127.0.0.1:8000/

##Funcionalidades implementadas (MVP)

    Crear ticket

    Listar tickets

    Filtros por estado y prioridad

    Ver detalle de ticket

    Actualizar estado y prioridad

    Agregar comentarios

    Persistencia en base de datos SQLite

    Autenticación y control de acceso básico por rol

##Estructura básica

    Modelo Ticket con estados y prioridades definidos mediante TextChoices.

    Modelo Comentario relacionado mediante ForeignKey.

    Uso de ModelForms.

    Control de acceso con @login_required.

##Uso de IA

    Se utilizó asistencia de inteligencia artificial como apoyo para revisión de código y optimización de implementación, manteniendo validación manual y comprensión de cada componente desarrollado.