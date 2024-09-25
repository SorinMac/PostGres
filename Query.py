import psycopg2

connection = psycopg2.connect(host="localhost", dbname="postgres", user="postgres", password="Q8yif7he", port=5433)

cur = connection.cursor()

cur.execute("""SELECT * FROM person WHERE name = 'Bob';""")

print(cur.fetchone())

connection.commit()

cur.close()

connection.close()