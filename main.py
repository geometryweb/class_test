import os
import sys
# sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from school.student import Student
from school.studentlist import StudentList

sl = StudentList()
sl.append(Student(100))
sl.append(Student(80))
sl.append(Student(70))
sl.print()
