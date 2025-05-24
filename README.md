# Red_Social_Microservicios

Aplicación de red social desarrollada con una arquitectura de microservicios, facilitando la escalabilidad, mantenibilidad y despliegue independiente de cada componente.

## 🚀 Tecnologías Utilizadas

- **Lenguaje de Programación:**
  - [Python](https://www.python.org/): Lenguaje principal para el desarrollo de los microservicios.

- **Frameworks y Bibliotecas:**
  - [FastAPI](https://fastapi.tiangolo.com/): Framework moderno y de alto rendimiento para la construcción de APIs con Python.
  - [SQLAlchemy](https://www.sqlalchemy.org/): Toolkit SQL y ORM para Python.

- **Base de Datos:**
  - [PostgreSQL](https://www.postgresql.org/): Sistema de gestión de bases de datos relacional utilizado por los servicios.

- **Contenedorización y Orquestación:**
  - [Docker](https://www.docker.com/): Plataforma para desarrollar, enviar y ejecutar aplicaciones en contenedores.
  - [Docker Compose](https://docs.docker.com/compose/): Herramienta para definir y administrar aplicaciones Docker multicontenedor.

## 📂 Estructura del Proyecto

```bash
Red_Social_Microservicios/
├── Api_Gateway/
├── Feed_Service/
├── Follow_Service/
├── Notification_Service/
├── Profile_Service/
├── docker-compose.yml
└── README.md
```

## 🧩 Descripción de los Microservicios

- **Api_Gateway:** Punto de entrada para las solicitudes de los clientes, encargado de enrutar las peticiones a los microservicios correspondientes y manejar aspectos transversales como autenticación y control de acceso.

- **Profile_Service:** Gestiona la información de los perfiles de los usuarios, incluyendo creación, actualización y recuperación de datos personales.

- **Follow_Service:** Maneja las relaciones de seguimiento entre usuarios, permitiendo seguir o dejar de seguir a otros miembros de la red.

- **Feed_Service:** Genera y proporciona el feed de publicaciones para los usuarios, recopilando contenido relevante basado en las relaciones de seguimiento.

- **Notification_Service:** Administra las notificaciones del sistema, informando a los usuarios sobre eventos importantes como nuevos seguidores o interacciones en sus publicaciones.

## 🛠️ Despliegue con Docker

Para facilitar el despliegue y la ejecución de los microservicios, se utiliza Docker y Docker Compose. A continuación, se detallan los pasos para levantar la aplicación en un entorno local:

1. **Clonar el repositorio:**

   ```bash
   git clone https://github.com/SanAJC/Red_Social_Microservicios.git
   cd Red_Social_Microservicios
   ```
1. **Construir y levantar los contenedores:**

   ```bash
   docker-compose up --build
   ```

