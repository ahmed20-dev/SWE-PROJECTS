
import psycopg2

conn = psycopg2.connect(
    host="localhost",
    dbname="postgres",
    user="postgres",
    password="1234",
    port="5432"
)





cur = conn.cursor()

# cur.execute("""
#     CREATE TABLE IF NOT EXISTS person (
#         id INT PRIMARY KEY,
#         name VARCHAR(255),
#         age INT,
#         gender CHAR
#     );
# """)

# conn.commit()




# cur = conn.cursor()

# cur.execute("""
#     INSERT INTO person (id, name, age, gender)
#     VALUES (1, 'Ahmed', 21, 'M');
# """)

# conn.commit()

# print("Person inserted successfully!")



cur.execute("SELECT * FROM person;")

rows = cur.fetchall()

for row in rows:
    print(row)

cur.close()
conn.close()