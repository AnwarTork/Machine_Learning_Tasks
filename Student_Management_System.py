"""Welcome To The Student Grades Managment System """
students = {}
name = ""
while True:
    name = input("Enter student name (or type 'done' to finish): ")
    if name == "done":
        break 
    else :
        grade = int(input(f"Enter {name}'s grade:"))

    students.setdefault(name,grade)

print(students)
for name , grade in students.items():
    print(f"{name} : {grade}")

def class_averaged_grade(dictionary):
    averaged_grade = sum(dictionary.values())/len(dictionary.values())
    return averaged_grade
def get_highest_lowest_grades(dictionary):
    highest_grade = max(dictionary.values()) 
    lowest_grade = min(dictionary.values())
    for key , value in dictionary.items():
        if value == highest_grade :
            print(f"The Highest grade is:{highest_grade}({key})")
        elif value == lowest_grade:
            print(f"The Lowest grade is:{lowest_grade}({key})")

def top_performing_student(dictionary):
    for key , value in dictionary.items():
        if value >= 90 and value <= 100 :
            print(f"{key} - {value}(Excellent)")
        elif value >= 75 and value <= 89 :
            print(f"{key} - {value}(Good)")
        elif value < 75 :
            print(f"{key} - {value}(Needs Improvement)")


print("Class Performance Report")
print("-------------------------")
print(f"Total Students:{len(students)}")
print(f"The Averaged Grade is:{class_averaged_grade(students)}")
# print(f"The Highest grade is:{get_highest_lowest_grades(students)[0]}")
# print(f"The Lowest grade is: {get_highest_lowest_grades(students)[1]}")
get_highest_lowest_grades(students)
print("Performance Breakdown:")
top_performing_student(students)