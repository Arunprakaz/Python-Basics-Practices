class student:
    def __init__(self, name, age): ##name , age variable are local variable, validity only inside INIT constructor
        self.username=age
        self.userage=name
        print("--- Inside Constructor")

    def display(self):
        print("Name is ", self.username) #note self.username is instance variable and name,age is local variable
        print("Age is ", self.userage)

    def __str__(self):
        return f"Name is {self.userage} and Age is {self.username}"

    # def display(self):
    #     print("Name is ", self.username)
   

s1=student("Arunprakash", 25)
print(s1.username)
print(s1)
s1.display()

# What happens if you define two methods with the same name in a class?
# Python does NOT support method overloading by name.
# 👉 The last method definition wins.
# The earlier one is completely overwritten.
# -----------------------------------------------------------------------------------------------------------------
# What happens if you don’t use self?

# This won’t work:

# def display(self):
#     print(username)  # ERROR

# Python doesn’t know which object’s username you mean. You must use self to specify the instance variable.