

Grades_passed = {}  # create an empty dictionary
Grades_failed = {}  # create an empty dictionary

num_students = int(input("Enter number of students: "))  # input number of students

for i in range(num_students): # loop to input student names and grades
    name = input("Enter name of student " + str(i + 1) + ": ")  # input student name
    grade = float(input("Enter grade of " + name + ": ")) # input student grade

    if grade >= 50:  # check if the student has passed
        Grades_passed[name] = grade # add student name and grade to dictionary if passed
    
    else:
        Grades_failed[name] = grade # add student name and grade to dictionary if failed

print("\nGrades of passed students are:")
for name, grade in Grades_passed.items():
    print(name,"has passed with grade:", grade)  # print student name and grade if passed

print("\nGrades of failed students are:")
for name, grade in Grades_failed.items():
    print(name,"has failed with grade:", grade)  # print student name and grade if failed