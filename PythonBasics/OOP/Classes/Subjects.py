import random

class Subject:
    def __init__(self,year,subject,students):
        self.year = year
        self.subject = subject
        self.students = students

    def add_subject(__init__, subject_name, subject_students, subject_year):
        subject_name = input("name: ")
        subject_year = input("year level: ")
        subject_students = random.randint(0, 30)

        def view_subject(new_subject_name, new_subject_year, no_subject_students):
            new_subject_name = str(subject_name)
            new_subject_year = int(subject_year)
            no_subject_students = int(subject_students)

            print(f'There are {no_subject_students} Students in Year {new_subject_year} {new_subject_name}')
            return new_subject_name, new_subject_year
        
        view_subject(new_subject_name=any, new_subject_year=any, no_subject_students=any)



        