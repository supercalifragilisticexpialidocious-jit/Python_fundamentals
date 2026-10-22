print("Hello, World!", "abhijit")
print(45+43)


name = "abhijit"
age = 25
cgpa = 9.8
age2 = 30
old = False
a = None

print(name, age, cgpa)
#type of variables

print(type(name))       #string
print(type(age))        #integer
print(type(cgpa))       #float
print(type(old))        #boolean
print(type(a))          #NoneType

name = input("Enter your name: ")
age = int(input("Enter your age: "))
cgpa = float(input("Enter your CGPA: ")) #comment

print(name, age, cgpa)  
print("hello " + name + ", your age is " + str(age) + " and your CGPA is " + str(cgpa)) #concatention

first_name = "Tony"
last_name = "Stark"
age = 53
height = 1.85 

superhero_name = input("Enter your superhero name: ")

print("Hello " + first_name + " " + last_name + ", your age is " + str(age) + " and your height is " + str(height) + ". Your superhero name is " + superhero_name)
