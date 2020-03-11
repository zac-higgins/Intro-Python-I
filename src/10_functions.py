# Write a function is_even that will return true if the passed-in number is even.


def is_even():
    # Read a number from the keyboard
    num = input("Enter a number: ")
    num = int(num)
    if num % 2 == 0:
        return True
    else:
        return False


# Print out "Even!" if the number is even. Otherwise print "Odd"


# YOUR CODE HERE
def print_even():
    if is_even():
        print("Even!")
    else:
        print("Odd")


print_even()
