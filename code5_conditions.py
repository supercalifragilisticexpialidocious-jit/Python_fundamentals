#conditional statements

age = 21
if(age >= 18):
    print("You are eligible to vote.")
    print("you can drive")

light = "pink"
if(light == "green"):
    print("Go")
elif(light == "yellow"):
    print("Slow down")      #indentation is important in python. It will give error if not properly indented.
elif(light == "red"):
    print("Stop")
else:
    print("Invalid light color")


num = 12

if(num > 6):
    print("Number is greater than 6")
if(num > 10):
    print("Number is greater than 10")
elif(num > 15):
    print("Number is greater than 15") #will only verify the first condition and not check the second one because the first condition is true.

#grades

marks = int(input("Enter your Marks: "))

if(marks >= 90):
    print("Your Grade is A")
elif(marks >= 80 and marks < 90):
    print("Your Grade is B")
elif(marks >= 70 and marks < 80):
    print("Your Grade is C")
elif(marks >= 60 and marks < 70):
    print("Your Grade is D")
else:
    print("Your Grade is F")

#nesting of if else statements

age = 65

if(age >= 18):
    if(age >= 60):
        print("You are a senior citizen")
    else:
        print("You are an adult")
else: 
    print("You are a minor")
