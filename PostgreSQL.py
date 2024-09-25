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

cur.execute("""INSERT INTO person (id, name, age, gender) VALUES
(1, 'Mike', 21, 'm'),          
(2, 'Bob', 22, 'm'),
(3, 'Joe', 23, 'm')       
""")

cur.execute("""SELECT * FROM person WHERE name = 'Bob';""")

print(cur.fetchone())

connection.commit()

cur.close()

connection.close()