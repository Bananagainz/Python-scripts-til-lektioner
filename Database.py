import sqlite3  # Importér SQLite3-modulet
from sqlite3 import Error  # Importér Error-klassen fra SQLite3-modulet

# Funktion til at oprette forbindelse til en database
def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)  # Opret forbindelse til databasen på den angivne sti
        print("Connection to SQLite DB successful")  # Udskriv meddelelse om vellykket forbindelse
    except Error as e:
        print(f"The error '{e}' occurred")  # Udskriv eventuelle fejl, der opstår under oprettelsen af forbindelsen
    return connection  # Returnér forbindelsen

# Opret forbindelse til databasen "school.db"
connection = create_connection("school.db")

# Funktion til at udføre en SQL-forespørgsel
def execute_query(connection, query):
    cursor = connection.cursor()  # Opret en cursor-objekt til at udføre forespørgslen
    try:
        cursor.execute(query)  # Udfør forespørgslen
        connection.commit()  # Bekræft ændringer i databasen
        print("Query executed successfully")  # Udskriv meddelelse om vellykket udførelse af forespørgslen
    except Error as e:
        print(f"The error '{e}' occurred")  # Udskriv eventuelle fejl, der opstår under udførelsen af forespørgslen

# SQL-forespørgsler til oprettelse af tabeller
create_students_table = '''CREATE TABLE IF NOT EXISTS Students (
                            student_id INTEGER PRIMARY KEY,
                            name TEXT NOT NULL,
                            major TEXT NOT NULL
                        )'''

create_courses_table = '''CREATE TABLE IF NOT EXISTS Courses (
                            course_id INTEGER PRIMARY KEY,
                            course_name TEXT NOT NULL,
                            instructor TEXT NOT NULL
                        )'''

create_enrollments_table = '''CREATE TABLE IF NOT EXISTS Enrollments (
                                enrollment_id INTEGER PRIMARY KEY,
                                student_id INTEGER NOT NULL,
                                course_id INTEGER NOT NULL,
                                FOREIGN KEY (student_id) REFERENCES Students (student_id),
                                FOREIGN KEY (course_id) REFERENCES Courses (course_id)
                            )'''

# Udfør SQL-forespørgslerne til oprettelse af tabeller
execute_query(connection, create_students_table)
execute_query(connection, create_courses_table)
execute_query(connection, create_enrollments_table)

# SQL-forespørgsler til indsættelse af data i tabellerne
create_students = """
INSERT INTO
  students (student_id, name, major)
VALUES
   (1, 'Alice', 'Computer Science'),
    (2, 'Bob', 'Mathematics'),
    (3, 'Charlie', 'Physics'),
    (4, 'David', 'Biology'),
    (5, 'Eve', 'Chemistry');
"""

create_courses = """
INSERT INTO
  courses (course_id, course_name, instructor)
VALUES
   (1, 'Python Programming', 'Dr. Smith'),
    (2, 'Calculus', 'Prof. Johnson'),
    (3, 'Quantum Mechanics', 'Dr. Brown'),
    (4, 'Genetics', 'Prof. Martinez'),
    (5, 'Organic Chemistry', 'Dr. White');
"""

create_enrollments = """
INSERT INTO
  enrollments (enrollment_id, student_id, course_id)
VALUES
     (1, 1, 1),
    (2, 2, 2),
    (3, 3, 3),
    (4, 4, 4),
    (5, 5, 5);
"""

# Udfør SQL-forespørgslerne til indsættelse af data
execute_query(connection, create_students)
execute_query(connection, create_courses)
execute_query(connection, create_enrollments)

# Funktion til at vælge alle kurser for en bestemt studerende
def select_courses_for_student(connection, student_name):
    cursor = connection.cursor()  # Opret en cursor-objekt
    cursor.execute("""
        SELECT Courses.course_name
        FROM Courses
        INNER JOIN Enrollments ON Courses.course_id = Enrollments.course_id
        WHERE Enrollments.student_id = (
            SELECT student_id FROM Students WHERE name = ?
        )
    """, (student_name,)) 
    rows = cursor.fetchall()  # Hent resultaterne fra forespørgslen
    return rows  # Returnér resultaterne

# Eksempel på brug af funktionen til at vælge kurser for en bestemt studerende
student_name = 'Alice'
courses = select_courses_for_student(connection, student_name)
print(f"Kurser for {student_name}:")
for course in courses:
    print(course[0])  # Udskriv navnene på kurserne

# Funktion til at vælge alle studerende, der er tilmeldt et specifikt kursus
def select_students_for_course(connection, course_name):
    cursor = connection.cursor()  # Opret en cursor-objekt
    cursor.execute("""
        SELECT Students.name
        FROM Students
        INNER JOIN Enrollments ON Students.student_id = Enrollments.student_id
        WHERE Enrollments.course_id = (
            SELECT course_id FROM Courses WHERE course_name = ?
        )
    """, (course_name,))  
    rows = cursor.fetchall()  # Hent resultaterne fra forespørgslen
    return rows  # Returnér resultaterne

# Eksempel på brug af funktionen til at vælge studerende for et specifikt kursus
course_name = 'Calculus'
students = select_students_for_course(connection, course_name)
print(f"Studerende på kurset '{course_name}':")
for student in students:
    print(student[0])  # Udskriv navnene på de studerende
