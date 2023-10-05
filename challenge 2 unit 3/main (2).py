class student:

  def _init_(self, name, roll_number, cgpa):
    self.name = name
    self.roll_number = roll_number
    self.cgpa = cgpa


def sort_students(student_list):
  #sort the list of students in descending order of CGPA
  sorted_students = sorted(student_list, 
                           key=lambda student:student.cgpa, 
                           reverse=True)
  #syntax = lambda arg:exp
  return sorted_students


#example usage
students = [ 
   student("dhanam", "A123", 7.8),
   student("lakshmi", "A124", 8.9),
   student("deepa", "A125", 9.1),
   student("vaishu", "A126", 9.9),
]

sorted_students = sort_students(students)

#print the sorted list of students
for student in sorted_students:
  print("Name: {}, Roll_number: {},CGPA: {}".format(student.name, student.roll_number,
                                                    student.cgpa))