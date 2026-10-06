#print
print('My name is Hareesh..')
print("same")

#variables
#strings
first_name = 'Hareesh'
last_name = 'Reddy'
print(f"my name is {first_name} {last_name}")

#integers&floats
age=20.5
print(f"My age is {age} years old")

#boolean
is_student = True
if is_student:
 print(" Hareesh is a student") 

#Typecasting = its use to convert one data type to another data type. With functions like int(), float(), str(), bool() etc.
name="Hareesh"
age=20
gpa=9.8
is_student=True

age = float(age)
print(age)
age = str(age)
print(type(age))

bool = bool(name)
print(bool)
#it is used to check whether the string is empty or not. If the string is empty, it will return False, otherwise it will return True.
#In this case, since the name variable contains the string "Hareesh", the bool function will return True.

#input() = it is used to take input from the user.
# It always returns a string, so if you want to take a number as input, you need to typecast it to int or float.

name=input("Enter your name:")
age=input("What's your age: ")
print(f"Hello {name}!")
print(f"And my age is also", age)
name = input("What's your name? ").strip().title()
print(f"hello,{name}")