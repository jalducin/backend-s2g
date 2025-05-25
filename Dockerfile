FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
# Define la URL de tu BD apuntando al servicio 'db' de docker-compose
ENV DATABASE_URL="mysql+pymysql://root:DevOps25%@db/s2g_db"
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]