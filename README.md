Descripción corta del proyecto

#  Actividad 3 – Inserción Masiva de Datos con Python, Faker y MySQL

Este proyecto implementa la creación automática de una tabla en MySQL y la inserción de 100.000 registros utilizando **Python**, **SQLAlchemy** y **Faker**.  
La actividad se desarrolla en el entorno de un proyecto real de  datos, siguiendo buenas prácticas como:

- Uso de entornos virtuales.
- Manejo de credenciales mediante `.env`.
- Control de versiones con Git.
- Inserción eficiente mediante batch processing.
- Documentación clara y reproducible.

---

##  Características del proyecto

- Conexión automática a MySQL usando SQLAlchemy.
- Creación de la tabla: `personas_<tu_nombre>`  
- Generación de datos falsos realistas (es_CO).
- Inserción eficiente en lotes (batch size configurable).
- Borra automáticamente la tabla antes de generar nuevos datos (opcional).
- Total: **100.000 registros** exactos.
- Estructura organizada y modular.

---

##  Estructura de la tabla

La tabla `personas_<tu_nombre>` contiene las siguientes columnas:

| Campo       | Tipo        | Descripción                     |
|-------------|-------------|----------------------------------|
| id          | INT PK      | Identificador autoincremental   |
| nombre      | VARCHAR(100)| Nombre completo                 |
| correo      | VARCHAR(150)| Correo electrónico              |
| ciudad      | VARCHAR(100)| Ciudad                          |
| telefono    | VARCHAR(50) | Teléfono                        |
| ocupacion   | VARCHAR(100)| Trabajo u ocupación             |
| direccion   | VARCHAR(200)| Dirección generada por Faker    |
| edad        | INT         | Edad entre 18 y 90 años         |

---

##  Tecnologías utilizadas

- **Python 3.10+**
- **MySQL** (local)
- **SQLAlchemy**
- **PyMySQL**
- **Faker (es_CO)**
- **python-dotenv**
- **Visual Studio Code**
- **Git & GitHub**

---

##  Instalación y ejecución

###  Clonar el repositorio
```bash
git clone <url-del-repositorio >
cd <carpeta-del-proyecto >

### Crear y activar entorno virtual

Crear y activar entorno virtual

### instalar dependencias 

pip install -r requirements.txt

### Configurar variables de entorno

DB_USER=root
DB_PASS=tu_contrasena
DB_HOST=localhost
DB_PORT=3306
DB_NAME=actividad3


###Ejecutar el script principal

python main.py

