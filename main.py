import _sqlite3
conn = _sqlite3.connect('Liceum.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS students()
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER,
    major TEXT)''')
cursor.execute.('''CREATE TABLE IS NOT EXISTS curses(
    curse_id INTEGER PRIMARY KEY AUTOINCREMENT,
    curse_name TEXT,
    instructor TEXT)''')
cursor.execute('''CREATE TABLE IS NOT EXISTS curses_students(
    student_id INTEGER,
    curse_id INTEGER,
    FOREIGN KEY(student_id) REFERENCES students(id),
    FOREIGN KEY(curse_id) REFERENCES curses(curse_id)
    PRIMARY KEY(student_id, curse_id))''')

while True:
    print("1. Add new student")
    print("2. Add new course")
    print("3. Show students list")
    print("4. Show courses list")
    print("5. Register student")
    print("6. Show students on course")
    print("7. Exit")
