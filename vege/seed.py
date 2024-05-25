from faker import Faker
fake = Faker()
import random
from home.models import *

def seed_db(n=10) -> None:
 try:
    for _ in range(n):
        departmentObj=Department.objects.all()
        random_index=random.randint(0,len(departmentObj)-1)
        department=departmentObj[random_index]

        studentId=f'STU-0{random.randint(20,999)}'
        studentName=fake.name()
        studentEmail=fake.email()
        studentAge=random.randint(20,30)
        studentAddress=fake.address()


        studentIdObj=StudentId.objects.create(studentId=studentId)

        studentsObj=Students.objects.create(
            department =department,
            studentId=studentIdObj,
            studentName=studentName,
            studentEmail = studentEmail,
            studentAge = studentAge,
            studentAddress=studentAddress
        )
 except Exception as e:
     print(e)