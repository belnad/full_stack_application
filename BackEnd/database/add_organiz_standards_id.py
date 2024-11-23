import mysql.connector

connection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Supremetop12?",
    database = "SecurityNorms"
)

cursor = connection.cursor()

organizationStandarsID = [
    # France and his security standards
    (1, 1),
    (2, 2),

    # USA and his security standards
    (3, 3),
    (3, 4),

    #UK and his security standards
    (6, 5),
    (8, 6),
]

insert_sql = """
    INSERT INTO organization_standard (organization_id, standard_id)
    VALUES (%s,%s);
"""

cursor.executemany(insert_sql, organizationStandarsID)
connection.commit()

cursor.close()
connection.close()

print("The IDs have been sucessfully added.")