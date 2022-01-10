#Define a function that can accept an integer number as input and print the "It is an even number" if the number is even, otherwise print "It is an odd number".

def odd_even(number):
    if number %2 == 0:
        print("It is an even number")
    else:
        print("It is an odd number")

number = int(input("Enter a number: "))
odd_even(number)