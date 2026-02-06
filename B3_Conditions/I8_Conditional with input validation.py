# Conditional with input validation
user_input=input("Enter a number: ")

if user_input.isdigit():
 print("You entered a valid number", user_input)
else:   
 print("Invalid input. Please enter a valid number.",user_input)

try:
    number=int(user_input)
    if number>0:
        print("Positive number")
    elif number<0:
        print("Negative number")
    else:
        print("Zero")   
except ValueError:
    print("Invalid input. Please enter a valid number.",user_input)