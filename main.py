import _sqlite3
conn = _sqlite3.connect("Liceum.db")
cursor = conn.cursor()
cursor.execute("""CREATE TABLE IS NOT EXISTS students(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT, 
    age INTEGER, 
    major TEXT)""")
cursor.execute("""CREATE TABLE IS NOT EXISTS curses(
    curse_id INTEGER PRIMARY KEY AUTOINCREMENT,
    curse_name TEXT,
    instruktor TEXT)""")
cursor.execute("""CREATE TABLE IS NOT EXISTS student_curses(
    student_id INTEGER,
    curse_id INTEGER,
    FOREIGN KEY (student_id) REFERENCES students(id),
    FOREIGN KEY (curse_id) REFERENCES curses(curse_id),
    PRIMARY KEY (student_id, curse_id))""")

while True:
    print("1.Add new student")
    print("2.Add new curse")
    print("3.Show students list")
    print("4.Show curses list")
    print("5.Reg student")
    print("6.Show students on curse")
    print("7.Exit")
    choise = input("choise action 1-7: ")
    if choise == "1":
        name = input("add name")
        age = int(input("add age"))
        major = input("add major")
        cursor.execute("""INSERT INTO students(name, age, major) VALUES(?,?,?)""",(name, age, major))
        conn.commit()
    elif choise == "2":
        major_name = input("add major name")
        instruktor_name = input("add instructor name")
        cursor.execute("""INSERT INTO curses(curse_name, instruktor) VALUES(?,?)"""(major_name, instruktor_name))
        conn.commit()
    elif choise == "3":
        cursor.execute("""SELECT * FROM students""")
        student = cursor.fetchall()
        if not student:
            print("Студентів нема")
        else:
            for st in student:
                print(f"id:{st[0]}, name: {st[1]}, age: {st[2]}, major: {st[3]}")
    elif choise == "4":
        cursor.execute("""SELECT * FROM curses""")
        curses = cursor.fetchall()
        if not curses:
            print("Курсів немає")
        else:
            for cs in curses:
                print(f"id:{cs[0]}, major_name: {cs[1]}, instruktor: {cs[2]}")
    elif choise == "5":
        student_id = int(input("add student id"))
        curse_id = int(input("add major id"))
        cursor.execute("""INSERT INTO student_curses(student_id, curse_id)VALUES(student_id, curse_id)""")
        conn.commit()
    elif choise == "6":
        curse_id = int(input("add major id"))
        cursor.execute("""SELECT students.id, students.name, students.age, studens.major
                       FROM students, student_curses
                       WHERE students.id = student_curses.student_id
                       AND student_curses.curse_id = ?""",(curse_id))
        students_on_curse = cursor.fetchall()
        if not students_on_curse:
            print("На курсі немає студентів")
        else:
            for st in students_on_curse:
                print(f"id:{st[0]}, name: {st[1]}, age: {st[2]}, major: {st[3]}")
    elif choise == "7":
        break
conn.close()