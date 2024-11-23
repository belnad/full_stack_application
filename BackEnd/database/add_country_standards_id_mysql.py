import mysql.connector

connection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Supremetop12?",
    database = "SecurityNorms"
)

cursor = connection.cursor()

countryStandarsID = [
    # France and his security standards
    (7, 1),
    (7, 2),

    # USA and his security standards
    (8, 3),
    (8, 4),

    #UK and his security standards
    (9, 5),
    (9, 6),
]

insert_sql = """
    INSERT INTO country_standards (country_id, standard_id)
    VALUES (%s,%s);
"""

cursor.executemany(insert_sql, countryStandarsID)
connection.commit()

cursor.close()
connection.close()

print("The IDs have been sucessfully added.")