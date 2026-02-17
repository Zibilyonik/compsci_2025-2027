student = 'bob' #global variable
student_list = ['bobby', 'sally', 'mary']

print('Var student before loop: ',student)

for student in student_list:
    print('For loop: ',student)

print('Var student after loop: ',student)

def get_student(student_name):
    student = 'sally' #local variable
    print('In function student_name: ',student_name)
    return student

print('Var student after def of function: ',student,"\n")

print('Get student return 1: ',get_student(student))
print('Var student after function call 1: ',student,'\n') 

print('Get student return 1: ',get_student('mary')) #what's this? Will be in the proggramming task
print('Var student after function call 2: ',student) 

# variable_list = [1, 1, 2, 3, 5, 8, 13, 21]