import psycopg2

try:
    conn = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="postgres",
        host="localhost",
        port="5432"
    )
    print("Verbindung erfolgreich!")
    conn.close()
except psycopg2.OperationalError as e:
    print("Fehler:", e)
