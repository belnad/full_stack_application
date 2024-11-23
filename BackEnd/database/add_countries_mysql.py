import mysql.connector

# Connexion à la base de données
connection = mysql.connector.connect(
    host="localhost",       # Adresse du serveur de base de données
    user="root",            # Nom d'utilisateur MySQL
    password="Supremetop12?",  # Mot de passe MySQL
    database="SecurityNorms"  # Nom de ta base de données
)

# Création d'un curseur pour exécuter les requêtes SQL
cursor = connection.cursor()

# Add several countries at the same time
countries = [
    ("United States of America", "USA"),
    ("United Kingdom", "UK"),
    ("France", "FR")
]

# Requête d'insertion SQL
insert_query = """
    INSERT INTO countries (country_name, iso_code)
    VALUES (%s, %s);
"""

# Exécution de la requête
cursor.executemany(insert_query, countries)

# Valider les changements
connection.commit()

#Close the cursor and the connection
cursor.close()
connection.close()

print("The new contries have been successfully added")
