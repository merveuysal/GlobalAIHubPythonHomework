
class Student():
    def __init__(self, namesurname):
        self.namesurname = namesurname
        self.courses = []

    def welcome_student(self):
        print("welcome, ", self.namesurname)

    def add_courses(self, newcourse):
        self.courses.append(newcourse)

    def calculate_grade(self):
        midterm = 10
        final = 5
        project = 7
        average = (midterm*0.3)+(final*0.5)+(project*0.2)
        print({"Midterm": midterm, "Final": final, "Project": project})
        return (average)
student1 = Student("Merve Uysal")
namesurname=input("Please enter your name and surname:")
namecounter=0

if namesurname != student1.namesurname:
    while namecounter < 2:

        namesurname = input("Please enter your name and surname:")
        namecounter += 1
if namesurname == student1.namesurname:

    def num_course_check(num_of_courses):
        if num_of_courses < 3:
            return ("You failed in class")

        for i in range(num_of_courses):
            if 3 <= num_of_courses <= 5:
                student1.add_courses(input("Please enter the course you want to choose: "))

    num_course_check(int(input("How many courses you want to choose? You choose minimum 3 and maximum 5 courses: ")))

else:
    print("Please try again later")
    exit()

selectedcourse = input("Please select one of these courses to take exams: ")

if student1.calculate_grade()>=90:
    print("You got AA, Congrats!!!")
elif 70<=student1.calculate_grade()<90:
    print("You got BB")
elif 50<=student1.calculate_grade()<70:
    print("You got CC")
elif 30<=student1.calculate_grade()<50:
    print("You got DD")
else:
    print("You got FF, You failed!!!")


