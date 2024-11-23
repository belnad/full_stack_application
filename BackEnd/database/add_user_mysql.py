import mysql.connector

# Connexion à la base de données
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Supremetop12?",
    database="SecurityNorms"
)

# Création d'un curseur pour exécuter les requêtes SQL
cursor = connection.cursor()

# When you want to add more than one users at the same time in your database
users = [
    ("bellad", "bellad@example.com", "plain_password", "user"),
    ("bonita23", "bonita@example.com", "password", "user")
]
# Données de l'utilisateur


# When you want to add just one user (Remove the # )

#username = "mirag"
#email = "mirag@example.com"
#password = "plain"
#role = "user"

# Requête d'insertion SQL
insert_query = """
    INSERT INTO users (username, email, password_hash, role)
    VALUES (%s, %s, %s, %s);
"""

# Exécution de la requête
cursor.executemany(insert_query, users)

# Valider les changements
connection.commit()

# Fermer le curseur et la connexion
cursor.close()
connection.close()

print("Les utilisateurs ont été ajouté avec succès.")
