FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7
WORKDIR /app

# Copier les dépendances pour l’API et la Database
COPY API/requirements.txt ./API/


# Installer les dépendances
RUN pip install --no-cache-dir -r ./API/requirements.txt


# Copier le code de l'application
COPY API /app/API
COPY database /app/database

# Exposer le port (8000 si vous utilisez FastAPI, ajustez-le en fonction de votre API)
EXPOSE 8000

# Commande pour lancer l'application (ajustez en fonction de votre projet)
CMD ["uvicorn", "API.main:app", "--host", "0.0.0.0", "--port", "8000"]
