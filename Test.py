"""Under 18 shall not pass"""
def main(name, birth):
    """main function"""
    if name == "A A":
        print("Welcome " + name + " to NongGipsy Pub")
    elif (2021 - birth) < 18:
        print("You shall not pass!")
    else:
        print("Welcome " + name + " to NongGipsy Pub")

main(input(), int(input()))
