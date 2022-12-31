import sqlite3 as lite
con=lite.connect('mtica.db')
cur=con.cursor()
cur.execute("DROP TABLE IF EXISTS Cars")
cur.execute('''CREATE TABLE Cars(
         Id INT,Name TEXT,Price INT)''')
print("table cars created.")
cur.execute("INSERT INTO Cars VALUES(1,'Skoda',9000)")
cur.execute("INSERT INTO Cars VALUES(2,'Volva',29000)")
cur.execute("INSERT INTO Cars VALUES(3,'Bentley',250000)")
cur.execute("INSERT INTO Cars VALUES(4,'Citroen',21000)")
cur.execute("INSERT INTO Cars VALUES(5,'Hummer',41400)")
cur.execute("INSERT INTO Cars VALUES(6,'Volkswagen',21600)")
con.commit()
print("values in table car inserted.")


