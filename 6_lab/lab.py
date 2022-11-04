import sqlite3 as db

#conn = db.connect(':memory:')
#conn = db.connect('6_lab/my.db')

def add_record(cursor, data:tuple): 
    cursor.execute("INSERT INTO students (firstname, lastname) VALUES (?, ?)", data)

def delete_record(cursor, firstname):
    if isinstance(firstname, str):
        cursor.execute("DELETE FROM students WHERE firstname=?", (firstname, ))
    elif isinstance(firstname, tuple) and len(firstname)==2:
        cursor.execute("DELETE FROM students WHERE firstname=? OR firstname=?", firstname)
    else:
        print("Непідходящі дані")

def show_all_records(cursor):
    return cursor.execute("SELECT * FROM students;").fetchall()

def get_first_result(cursor, condition):
    return cursor.execute("SELECT stdid, firstname FROM students WHERE lastname=? ORDER BY firstname ASC;", (condition, )).fetchone()

with db.connect('my.db') as conn:
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS students (stdid INTEGER PRIMARY KEY, firstname NVARCHAR(20), lastname NVARCHAR(20))")
    for record in [("Student_1", "TK"), ('Bohdan', 'BB'), ('Bogdan', 'BB'), ('Bobas', 'BB')]:
        add_record(c, record)
    

    c.execute("SELECT name FROM sqlite_master WHERE type='table';")
    print(c.fetchall())

    print(show_all_records(c))
    print(get_first_result(c, "BB"))

    delete_record(c, ("Student_1", "Bohdan"))
    delete_record(c, ("asd", "sfsd", "sdfsd"))
    
    print(show_all_records(c))




### Тут ми будемо працювати з базою

#conn.commit()
#conn.close()