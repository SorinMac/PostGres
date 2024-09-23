import psycopg2

connection = psycopg2.connect(host="localhost", dbname="postgres", user="postgres", password="Q8yif7he", port=5433)

cur = connection.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS person (
            id INT PRIMARY KEY,
            name VARCHAR(255),
            age INT,
            gender CHAR
);
""")

connection.commit()

cur.close()

connection.close()