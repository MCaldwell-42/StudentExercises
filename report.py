import sqlite3

class Student():

    def __init__(self, first, last, handle, cohort):
        self.first_name = first
        self.last_name = last
        self.slack_handle = handle
        self.cohort = cohort

    def __repr__(self):
        return f'{self.first_name} {self.last_name} is in {self.cohort}'

class Instructor():

    def __init__(self, first, last, handle, specialty, cohort):
        self.first_name = first
        self.last_name = last
        self.slack_handle = handle
        self.specialty = specialty
        self.cohort = cohort

    def __repr__(self):
        return f'{self.first_name} {self.last_name} is teaching {self.cohort}'

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
 
    def all_instructors(self):

        """Retrieve all instructors with the cohort name"""

        with sqlite3.connect(self.db_path) as conn:
            # using lambda:
            conn.row_factory = lambda cursor, row: Instructor(
    row[1], row[2], row[3], row[5], row[6]
)
            db_cursor = conn.cursor()


            db_cursor.execute("""
            select i.Id,
                i.FirstName,
                i.LastName,
                i.SlackHandle,
                i.CohortId,
                i.Specialty,
                c.Name
            from Instructor i
            join Cohort c on i.CohortId = c.Id
            order by i.CohortId
            """)

            all_instructors = db_cursor.fetchall()

            for instructor in all_instructors:
                print(instructor)
    
    
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

        """Retrieve all exercises"""

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
    
    
    def JavaScript_exercises(self):

        """Retrieve all javascript exercises"""

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
            where e.Language = "JavaScript"
            """)

            all_exercises = db_cursor.fetchall()

            for exercise in all_exercises:
                print(exercise)


    def Python_exercises(self):

        """Retrieve all python exercises"""

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
            where e.Language = "Python"
            """)

            all_exercises = db_cursor.fetchall()

            for exercise in all_exercises:
                print(exercise)


    def C_exercises(self):

        """Retrieve all C# exercises"""

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
            where e.Language = "C#"
            """)

            all_exercises = db_cursor.fetchall()

            for exercise in all_exercises:
                print(exercise)


    def ExerciseStudents(self):

        exercises = dict()

        with sqlite3.connect(self.db_path) as conn:
            db_cursor = conn.cursor()

            db_cursor.execute("""
                select
                    e.Id ExerciseId,
                    e.Name,
                    s.Id,
                    s.FirstName,
                    s.LastName
                from Exercise e
                join StudentExercise se on se.ExerciseId = e.Id
                join Student s on s.Id = se.StudentId
            """)

            dataset = db_cursor.fetchall()

            for row in dataset:
                exercise_id = row[0]
                exercise_name = row[1]
                student_id = row[2]
                student_name = f'{row[3]} {row[4]}'
                if exercise_name not in exercises:
                    exercises[exercise_name] = [student_name]
                else:
                    exercises[exercise_name].append(student_name)
            for exercise_name, students in exercises.items():
                print(exercise_name)
                for student in students:
                    print(f'\t* {student}')


    def StudentExercises(self):

        students = dict()

        with sqlite3.connect(self.db_path) as conn:
            db_cursor = conn.cursor()

            db_cursor.execute("""
                select
                    e.Id ExerciseId,
                    e.Name,
                    s.Id,
                    s.FirstName,
                    s.LastName
                from Exercise e
                join StudentExercise se on se.ExerciseId = e.Id
                join Student s on s.Id = se.StudentId
            """)

            dataset = db_cursor.fetchall()

            for row in dataset:
                exercise_id = row[0]
                exercise_name = row[1]
                student_id = row[2]
                student_name = f'{row[3]} {row[4]}'
                if student_name not in students:
                    students[student_name] = [exercise_name]
                else:
                    students[student_name].append(exercise_name)
            for student_name, exercises in students.items():
                print(f'{student_name} is working on:')
                for exercise in exercises:
                    print(f'\t* {exercise}')


    def InstructorExercises(self):

        instructors = dict()

        with sqlite3.connect(self.db_path) as conn:
            db_cursor = conn.cursor()

            db_cursor.execute("""
                select
                    e.Id ExerciseId,
                    e.Name,
                    i.Id,
                    i.FirstName,
                    i.LastName
                from Exercise e
                join StudentExercise se on se.ExerciseId = e.Id
                join Instructor i on i.Id = se.InstructorId
            """)

            dataset = db_cursor.fetchall()

            for row in dataset:
                exercise_id = row[0]
                exercise_name = row[1]
                instructor_id = row[2]
                instructor_name = f'{row[3]} {row[4]}'
                if instructor_name not in instructors:
                    instructors[instructor_name] = [exercise_name]
                else:
                    if exercise_name not in instructors[instructor_name]:
                        instructors[instructor_name].append(exercise_name)
                    else:
                        pass
            for instructor_name, exercises in instructors.items():
                print(f'{instructor_name} has assigned:')
                for exercise in exercises:
                    print(f'\t* {exercise}')


    def ErbodyExercises(self):

        exercises = dict()

        with sqlite3.connect(self.db_path) as conn:
            db_cursor = conn.cursor()

            db_cursor.execute("""
                select
                    e.Id ExerciseId,
                    e.Name,
                    i.Id InstructorId,
                    i.FirstName,
                    i.LastName,
                    s.FirstName,
                    s.LastName,
                    s.Id
                from Exercise e
                join StudentExercise se on se.ExerciseId = e.Id
                join Instructor i on i.Id = se.InstructorId
                join Student s on s.Id = se.StudentId
            """)

            dataset = db_cursor.fetchall()

            for row in dataset:
                exercise_id = row[0]
                exercise_name = row[1]
                instructor_id = row[2]
                instructor_name = f'{row[3]} {row[4]}'
                student_name = f'{row[5]} {row[6]}'
                student_id = row[7]
                if exercise_name not in exercises:
                    exercises[exercise_name] = [(instructor_name, student_name)]
                else:
                    if ([instructor_name], [student_name]) not in exercises[exercise_name]:
                        exercises[exercise_name].append((instructor_name, student_name))
                    else:
                        pass
            for exercise_name, couples in exercises.items():
                print(f'{exercise_name}:')
                for couple in couples:
                    print(f'\t* {couple[0]} assigned this to {couple[1]}')


    def CohortReport(self):

        cohorts = dict()

        with sqlite3.connect(self.db_path) as conn:
            db_cursor = conn.cursor()

            db_cursor.execute("""
                select
                    c.Id CohortId,
                    c.Name,
                    i.Id InstructorId,
                    i.FirstName,
                    i.LastName,
                    s.FirstName,
                    s.LastName
                from Cohort c
                join Instructor i on i.CohortId = c.Id
                join Student s on s.CohortId = c.Id
            """)

            dataset = db_cursor.fetchall()

            for row in dataset:
                cohort_id = row[0]
                cohort_name = row[1]
                instructor_id = row[2]
                instructor_name = f'{row[3]} {row[4]}'
                student_name = f'{row[5]} {row[6]}'
                if cohort_name not in cohorts:
                    cohorts[cohort_name] = {"instructors": [instructor_name], "students": [student_name] }
                else:
                    if instructor_name not in cohorts[cohort_name]["instructors"]:
                        cohorts[cohort_name]["instructors"].append(instructor_name)
                    else:
                        pass

                    if student_name not in cohorts[cohort_name]["students"]:
                        cohorts[cohort_name]["students"].append(student_name)
                    else:
                        pass

            for cohort_name, people in cohorts.items():
                print(f'{cohort_name}:')
                print(f'\t instructors:')
                for instructor in people["instructors"]:
                        print(f'\t* {instructor} is a teacher in {cohort_name}')
                print(f'\t students:')
                for student in people["students"]:
                        print(f'\t* {student} is a student in {cohort_name}')


#     def filtered_exercises(self, language):

#         """Retrieve all cohort names"""

#         with sqlite3.connect(self.db_path) as conn:
#             # using lambda:
#             conn.row_factory = lambda cursor, row: Exercise(
#     row[1], row[2]
# )
#             db_cursor = conn.cursor()


#             db_cursor.execute(f"""
#             select e.Id,
#                 e.Name,
#                 e.Language
#             from Exercise e
#             where e.Language = {self.language}
#             """)

#             all_exercises = db_cursor.fetchall()

#             for exercise in all_exercises:
#                 print(exercise)


reports = StudentExerciseReports()
# reports.all_students()
# reports.all_cohorts()
# reports.all_exercises()
# reports.JavaScript_exercises()
# reports.filtered_exercises('JavaScript')  THIS ISN'T WORKING
# reports.all_instructors()
# reports.ExerciseStudents()
# reports.StudentExercises()
# reports.InstructorExercises()
# reports.ErbodyExercises()
reports.CohortReport()

# student = Student('Bart', 'Simpson', '@bart', 'Cohort 8')
# print(f'{student.first_name} {student.last_name} is in {student.cohort}')

