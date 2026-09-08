print("Hello from mycode!")

person = "Elizabeth"

def say_hi(name: str) -> None:
    print(f"Hello, {name}!")


# if you call say_hi("Tom"), it will print:
# "Hello, Tom!"

def add(numbers: list[float]) -> float: 
    return sum(numbers)

# test add
def test_add():
    # test 1
    number = [1,2,3,4,5]
    result = add(number)
    assert result == 15, f"Expected 15, but got {result}"
    # test 2
    number = [0]
    result = add(number)
    assert result == 0, f"Expected 0, but got {result}"

# run your tests
if __name__ == "__main__":
    print("Running tests...")
    test_add()
# ^^ what this does is when you import it it doesnt run, if you click in module and run it it runs
# better so that test_add() doesn't test everytime you run it
