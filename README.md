# Backend - S2G Energy Challenge

**Repositorio:** [https://github.com/jalducin/backend-s2g](https://github.com/jalducin/backend-s2g)

---

## Tecnologías

* **Lenguaje:** Python 3.11
* **Framework web:** FastAPI
* **ORM:** SQLAlchemy
* **Base de datos:** MySQL (dockerizado)
* **Tareas programadas:** APScheduler
* **Gestión de configuración:** python-dotenv
* **Autenticación:** python-jose (JWT)
* **Contenedores:** Docker & Docker Compose
* **Validación de datos:** Pydantic (<2.0)

---

## Características

* **Autenticación JWT** con usuario/contraseña hardcoded.
* **CRUD de estaciones** de carga: registrar, listar y actualizar estado (activo/inactivo).
* **Estadísticas** en tiempo real (`GET /stations/stats`): total, activos, inactivos, suma de kW.
* **Scheduler automático** que alterna estados cada minuto y **endpoint manual** para dispararlo (`POST /scheduler/run`).
* **Carga de datos de ejemplo** desde CSV mediante `scripts/seed.py`.
* **Docker Compose** orquesta los servicios `db` (MySQL) y `backend` (FastAPI).

---

## Arquitectura

```txt
+-------------+      +---------------+      +--------------+
|  Cliente UI | <--> |  FastAPI API  | <--> |   MySQL DB   |
+-------------+      +---------------+      +--------------+
                             |
                             v
                  +----------------------+
                  |    APScheduler job   |
                  +----------------------+
```

---

## Estructura de carpetas

```bash
backend-s2g/
├── app/
│   ├── core/           # Configuración, DB, scheduler
│   ├── models/         # Modelos SQLAlchemy
│   ├── routers/        # Endpoints (auth, stations, stats, scheduler)
│   └── schemas/        # Pydantic schemas
├── data/               # CSV de datos de ejemplo
├── scripts/            # Seed script
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .env                # Variables de entorno
└── README.md
```

---

## Requisitos

* Docker (>=20.10)
* Docker Compose (>=1.29)
* (Opcional) Python 3.11 para ejecución local sin contenedores

---

## Variables de entorno

Crea un archivo `.env` en la raíz con:

```dotenv
MYSQL_ROOT_PASSWORD=DevOps25%
MYSQL_DATABASE=s2g_db
DATABASE_URL=mysql+pymysql://root:DevOps25%@db/s2g_db
SECRET_KEY=<tu_clave_secreta>
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=720
```

---

## Instalación y ejecución

### Con Docker Compose

```bash
# Limpia instancias anteriores
docker-compose down --volumes --remove-orphans

# Construye y levanta servicios
docker-compose up -d --build

# Verifica que estén en "Up"
docker-compose ps

# Espera a que MySQL esté listo y luego carga datos de ejemplo:
docker exec -it --workdir /app s2g-backend python -m scripts.seed

# Accede a la documentación interactiva:
http://localhost:8000/docs
```

### Sin Docker Compose (solo Docker)

```bash
# Construye la imagen (desde la raíz)
docker build -t s2g-backend .

# Lanza el contenedor vinculado a MySQL externo
docker run \
  -e DATABASE_URL=mysql+pymysql://root:DevOps25%@host.docker.internal:3306/s2g_db \
  -p 8000:8000 s2g-backend
```

---

## Endpoints

### Autenticación y autorización

* **POST** `/auth/login`
  Form data: `username`, `password`
  -> `{ "access_token": "<token>", "token_type": "bearer" }`

### Estaciones (requieren token Bearer)

* **POST** `/stations/`
  Crea estación. Body JSON: `{ name, location, max_kw, status }`
* **GET** `/stations/`
  Lista todas las estaciones.
* **PATCH** `/stations/{id}`
  Actualiza `status` (`?status=activo|inactivo`).
* **GET** `/stations/stats`
  Estadísticas agregadas.

### Scheduler

* **POST** `/scheduler/run`
  Ejecuta manualmente el job de cambio de estado.

---
## 👨‍💻 Autor

**Elaborado por ISC Juan Valentín Alducin Vázquez**  
📅 Mayo 2025  
🔗 [GitHub](https://github.com/jalducin)
## Git
git add .
git commit -m "Actualización BackendS2Energy"
git push origin main

## Licencia

MIT
