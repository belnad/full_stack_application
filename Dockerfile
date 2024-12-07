FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

# Copier les fichiers de dépendances
ADD requirements.txt /app/requirements.txt

# Installer les dépendances
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copier tout le dossier Backend
COPY ./Backend /app

# Définir le répertoire de travail
WORKDIR /app/API

# Exposer le port par défaut de FastAPI
EXPOSE 8000

# Commande de lancement
CMD ["uvicorn", "API.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
