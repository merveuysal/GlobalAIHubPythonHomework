first_name = input("Please enter your first name:")
last_name = input("Please enter your last name:")
age = int(input("Please enter your age:"))
birth_date = int(input("Please enter your birth year:"))

user_info = [first_name, last_name, age, birth_date]
for i in user_info:
    print(i)

if age<18:
    print("You can't go out because it's dangerous")
elif age>=18:
    print("You can go out to the street")
else:
    print("Invalid entry")
