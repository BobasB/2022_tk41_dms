import sqlite3 as db

#conn = db.connect(':memory:')
#conn = db.connect('6_lab/my.db')

with db.connect('my.db') as conn:
    c = conn.cursor()
    c.execute("CREATE TABLE students (stdid INTEGER PRIMARY KEY, firstname NVARCHAR(20), lastname NVARCHAR(20))")
    c.execute("INSERT INTO students VALUES (1, 'Bohdan', 'BB')")
    c.execute("INSERT INTO students VALUES (2, 'Bohdan', 'BB')")
    c.execute("INSERT INTO students VALUES (3, 'Bohdan', 'BB')")

    c.execute("SELECT name FROM sqlite_master WHERE type='table';")

    print(c.fetchall())

    c.execute("SELECT * FROM students;")

    print(c.fetchall())




### Тут ми будемо працювати з базою

#conn.commit()
#conn.close()