# 🎫 Ticket System – Django

Sistema de gestión de tickets desarrollado en Django como prueba técnica.  
Permite administrar incidencias mediante un flujo básico de creación, seguimiento y actualización, incluyendo gestión de comentarios asociados a cada ticket.

La aplicación implementa autenticación, control de acceso y persistencia en base de datos relacional.

---

## 🚀 Stack Tecnológico

- Python 3.12
- Django 6.0.2
- SQLite (entorno local)
- Docker & Docker Compose
- HTML5 / CSS3 / JS (Django Templates)

---

## 🏗 Arquitectura

El proyecto sigue el patrón MVT (Model–View–Template) de Django.

### Modelos principales

- **Ticket**
  - Título
  - Descripción
  - Estado (TextChoices)
  - Prioridad (TextChoices)
  - Fecha de creación
  - Usuario creador

- **Comentario**
  - Relación ForeignKey con Ticket
  - Autor
  - Contenido
  - Fecha de creación

### Componentes técnicos implementados

- ModelForms para validación
- Autenticación integrada de Django
- Protección CSRF
- Decoradores `@login_required`
- Separación de entorno mediante contenedores Docker

---

## ⚙️ Ejecución en entorno local (modo desarrollo)

### 1️⃣ Clonar repositorio

```bash
git clone <URL_DEL_REPOSITORIO>
cd ticket_system

### 2️⃣ Crear entorno virtual

python -m venv venv


### 3️⃣ Activar entorno virtual

venv\Scripts\activate

### 4️⃣ Instalar dependencias

pip install -r requirements.txt

### 5️⃣ Aplicar migraciones

python manage.py migrate

### 6️⃣ Crear superusuario (recomendado)

python manage.py createsuperuser

### 7️⃣ Ejecutar servidor

python manage.py runserver

Aplicación disponible en: http://127.0.0.1:8000/

## 
🐳 Ejecución con Docker
Requisitos

    * Docker Desktop

    * Docker Compose

### 1️⃣ Levantar entorno

docker compose up --build

Aplicación disponible en: http://localhost:8000/


### ✅ Funcionalidades Implementadas (MVP)

    Crear ticket

    Eliminar ticket

    Listar tickets

    Filtros por estado y prioridad

    Ver detalle de ticket

    Actualizar estado y prioridad

    Agregar comentarios

    Autenticación de usuarios

    Control de acceso

    Persistencia en SQLite

### 🔐 Seguridad Implementada

    Protección CSRF

    Validación de formularios en backend

    Restricción de vistas mediante autenticación

    Manejo seguro de sesiones


### 📦 Estructura del Proyecto
    ticket_system/
    │
    ├── config/            # Configuración principal Django
    ├── tickets/           # Aplicación principal
    ├── static/            # Archivos estáticos
    ├── templates/         # Plantillas
    ├── Dockerfile
    ├── docker-compose.yml
    └── requirements.txt

### 📌 Posibles Mejoras Futuras

    Separación de settings (dev/prod)

    Uso de variables de entorno (.env)

    Migración a PostgreSQL

    Implementación de permisos por rol más granular

    Exposición de API REST con Django REST Framework

    Implementación de pruebas automatizadas


### 🤖 Uso de Inteligencia Artificial

    Se utilizó asistencia de IA como herramienta de apoyo para optimización de código, manteniendo validación manual, comprensión y control total sobre la arquitectura y decisiones técnicas adoptadas, la unica inteligencia artificial utilizada fue ChatGPT.
