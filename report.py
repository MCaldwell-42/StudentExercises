import sqlite3

class Student():

    def __init__(self, first, last, handle, cohort):
        self.first_name = first
        self.last_name = last
        self.slack_handle = handle
        self.cohort = cohort

    def __repr__(self):
        return f'{self.first_name} {self.last_name} is in {self.cohort}'

class Cohort():

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'{self.name}'

class Exercise():

    def __init__(self, name, language):
        self.name = name
        self.language = language

    def __repr__(self):
        return f'{self.name} is a {self.language} exercise'

class StudentExerciseReports():

    """Methods for reports on the Student Exercises database"""

    def __init__(self):
        self.db_path = "/Users/user/workspace/python/StudentExercises/studentexercises.db"

    # def create_student(self, cursor, row):
    #     return Student(row[1], row[2], row[3], row[5])

    def all_students(self):

        """Retrieve all students with the cohort name"""

        with sqlite3.connect(self.db_path) as conn:
            # using lambda:
            conn.row_factory = lambda cursor, row: Student(
    row[1], row[2], row[3], row[5]
)
            db_cursor = conn.cursor()


            db_cursor.execute("""
            select s.Id,
                s.FirstName,
                s.LastName,
                s.SlackHandle,
                s.CohortId,
                c.Name
            from Student s
            join Cohort c on s.CohortId = c.Id
            order by s.CohortId
            """)

            all_students = db_cursor.fetchall()

            for student in all_students:
                print(student)
    
    
    def all_cohorts(self):

        """Retrieve all cohort names"""

        with sqlite3.connect(self.db_path) as conn:
            # using lambda:
            conn.row_factory = lambda cursor, row: Cohort(
    row[1]
)
            db_cursor = conn.cursor()


            db_cursor.execute("""
            select c.Id,
                c.Name
            from Cohort c
            """)

            all_cohorts = db_cursor.fetchall()

            for cohort in all_cohorts:
                print(cohort)
    
    
    def all_exercises(self):

        """Retrieve all cohort names"""

        with sqlite3.connect(self.db_path) as conn:
            # using lambda:
            conn.row_factory = lambda cursor, row: Exercise(
    row[1], row[2]
)
            db_cursor = conn.cursor()


            db_cursor.execute("""
            select e.Id,
                e.Name,
                e.Language
            from Exercise e
            """)

            all_exercises = db_cursor.fetchall()

            for exercise in all_exercises:
                print(exercise)

reports = StudentExerciseReports()
# reports.all_students()
# reports.all_cohorts()
reports.all_exercises()