import psycopg2

conn = psycopg2.connect(
    dbname="M122_LB1",
    user="nicol",
    password="LB1Nico",
    host="localhost",
    port="5432"
)

print("Erfolgreich verbunden!")
conn.close()