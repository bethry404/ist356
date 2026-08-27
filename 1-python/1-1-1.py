name = input("Enter your name: ")
print("Hello, " + name + "! Welcome to the program.")


# duck typing
age = 30    # assumes int
gpa = 3.4   # assumes float

# type cohersion
age = int("99")
gpa = float("3.4")

# age = input("Enter your age: ")    # type str

age = int(input("Enter your age: "))    # type int
pass