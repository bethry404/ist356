# this was how we built the algo for the function
# normally this goes away
numbers = [5,3,2,10]
total = sum(numbers)
count = len(numbers)
print(total) # 20
print(count) # 4
average = total / count
print(average) # 5.0


# and gets replaced with this
def average(numbers: list[float]) -> float: # <== input
    '''
    this function takes a list of numbers and returns the average of those numbers
    '''
    total = sum(numbers)
    count = len(numbers)
    average = total / count
    return average # <== output


# call the function
grades = [100,100,100,0]
result = average(grades)
print(result) # 75.0

average("low med high")


# method function has a variable.function(first argument is the variable itself)
# avoids using the wrong thing for the wrong type
name = "John"
name.capitalize() # JOHN
capitalize(name)