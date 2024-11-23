import mysql.connector

# Connexion à la base de données
connection = mysql.connector.connect(
    host="localhost",       # Adresse du serveur de base de données
    user="root",            # Nom d'utilisateur MySQL
    password="Supremetop12?",  # Mot de passe MySQL
    database="SecurityNorms"  # Nom de ta base de données
)

# Vérifier si la connexion est établie
if connection.is_connected():
    print("Successful connection to MySQL")
