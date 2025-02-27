# Aplicacion Kanban

Este proyecto consiste en un sistema Back-End desarrollado con Django.

---

## Tecnologías Utilizadas
- **Back-End:** Django REST Framework
- **Base de Datos:** PostgreSQL
- **Seguridad:** Autenticación Token

---

## Instrucciones de Instalación Backend
1. Clonar el repositorio

   ```bash
    git clone https://github.com/rjdrk/python_angular_test.git
    cd python_angular_test/back-end

2. Crear y activar un entorno virtual

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # Mac/Linux
    .\venv\Scripts\activate  # Windows

3. Instalar dependencias

    ```bash
    pip install -r requirements.txt

4. Configurar variables de entorno
    Crear el archivo .env en el directorio back-end y definir las variables necesarias:

    ```bash
    API_KEY=tu_api_key_secreta
    DB_NAME=tu_base_de_datos
    DB_USER=tu_usuario
    DB_PASSWORD=tu_pasword
    DB_HOST=tu_host
    DB_SCHEMA=-c search_path=tu_schema
    DB_PORT=5432

5. Configurar la base de datos
    Accede a PostgreSQL y crea la base de datos:

    ```bash
    CREATE DATABASE db_kanban;
    CREATE USER tu_usuario WITH PASSWORD 'tu_pasword';
    GRANT ALL PRIVILEGES ON DATABASE db_kanban TO your_user;
    CREATE SCHEMA kanban;


6. Aplicar migraciones

    ```bash
    python manage.py makemigrations
    python manage.py migrate

7. Crear un superusuario (opcional)

    ```bash
    python manage.py createsuperuser

8. Ejecutar el servidor

    ```bash
    python manage.py runserver

---

## Uso de la API
1. Endpoints Disponibles

| Método   | Endpoint                       | Descripción                      |
|----------|--------------------------------|----------------------------------|
| GET      | /api/tasks/                    | Obtener todas las tareas         |
| GET      | /api/tasks/<task_id>/	        | Obtener una tarea por su ID      |
| POST     | /api/tasks/create/	            | Crear una nueva tarea            |
| PUT      | /api/tasks/update/<task_id>/   | Actualizar una tarea existente   |
| DELETE   | /api/tasks/delete/<task_id>/   | Eliminar una tarea               |

2. Autenticación
    Todas las solicitudes deben incluir el header API-KEY:
        - **Key:** API-KEY  
        - **Value:** tu_api_key_secreta

---

## Ejemplo de Uso en Postman
**Authorization:** Ninguna (el API Key se pasa en Headers).

**Headers:**
    API-KEY: tu_api_key_secreta