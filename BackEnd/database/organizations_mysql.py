import mysql.connector

connection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Supremetop12?",
    database = "SecurityNorms"
)

# Creation of the cursor
cursor = connection.cursor()

# add some organiztions in the table
organizations = [
    ("ANSSI (Agence Nationale de la Sécurité des Systèmes d'Information)", 9, "C'est l'autorité nationale en matière de sécurité des systèmes d'information en France.Elle établit des recommandations, des référentiels et des normes en matière de cybersécurité pour les entités publiques et privées."),
    ("AFNOR (Association Française de Normalisation)", 9, "Organisme français de normalisation qui publie des normes de sécurité applicables aux systèmes d'information et aux entreprises."),
    
    ("NIST (National Institute of Standards and Technology)", 7, "L'institut américain de normalisation des technologies, connu pour publier des normes telles que le NIST Cybersecurity Framework et des séries de publications sur la cybersécurité"),
    ("CISA (Cybersecurity and Infrastructure Security Agency)", 7, "L'agence de cybersécurité des infrastructures critiques qui collabore avec le NIST pour définir et promouvoir les normes de sécurité."),
    ("ISO (International Organization for Standardization)", 7, "Bien que ce soit une organisation internationale, de nombreuses normes ISO (comme l'ISO 27001) sont largement adoptées aux États-Unis."),
    
    ("NCSC (National Cyber Security Centre)", 8, "Le NCSC est une entité du GCHQ (Government Communications Headquarters) qui établit des directives et des standards pour la cybersécurité au Royaume-Uni."),
    ("BSI (British Standards Institution)", 8, "L'organisme national de normalisation du Royaume-Uni, qui publie des normes de sécurité adoptées par les entreprises et le secteur public."),
    ("ISO", 8, "Tout comme aux États-Unis, les normes de l'ISO sont également très répandues et suivies au Royaume-Uni.")
]

# SQL Query
insert_query = """
    INSERT INTO organizations (organization_name, country_id, description)
    VALUES (%s, %s, %s);
"""

# Execute the changes
cursor.executemany(insert_query, organizations)
# commit the changes
connection.commit()

# Close the connection
cursor.close()
connection.close()

print("The organizations have been successfully added")