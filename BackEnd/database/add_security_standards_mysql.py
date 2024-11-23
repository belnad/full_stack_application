import mysql.connector

connection = mysql.connector.connect(
    host = "Localhost",
    user = "root",
    password = "Supremetop12?",
    database = "SecurityNorms"
)

cursor = connection.cursor()

securityStandards = [
    ("RGS", "Il établit les règles à respecter pour assurer la sécurité des systèmes d’information utilisés par les administrations publiques françaises. Il définit les exigences de sécurité et propose des solutions à mettre en œuvre.", 2010, "National", 1),
    ("ISO/IEC 27001", "Norme internationale pour le système de management de la sécurité de l'information, utilisée et promue par l'AFNOR en France", 2013, "International", 2),

    ("NIST SP 800-53 (Security and Privacy Controls for Federal Information Systems and Organizations)", "cette norme fournit un cadre pour sécuriser les systèmes d'information fédéraux.", 2020, "National", 3),
    ("NIST Cybersecurity Framework (CSF)", "Ce cadre de cybersécurité fournit des lignes directrices sur la manière de gérer et réduire les risques de cybersécurité", 2014, "National", 3),

    ("Cyber Essentials", "Une norme de sécurité informatique de base conçue par le gouvernement britannique pour aider les organisations à se protéger contre les cyberattaques courantes", 2014, "National", 6),
    ("ISO/IEC 27001", "Norme internationale pour la gestion de la sécurité de l'information, promue et certifiée par le BSI au Royaume-Uni", 2013, "International", 8)
]

insert_sql = """
    INSERT INTO security_standards (standard_name, description, year, type, organisationId)
    VALUES (%s,%s,%s,%s,%s);
"""

cursor.executemany(insert_sql, securityStandards)

connection.commit()

cursor.close()
connection.close()

print("The Norms have been successfully added.")