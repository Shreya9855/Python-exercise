#Write a method which can calculate square value of number

def Square(number):
    square = number ** 2
    return square

n  = int(input("Enter the number you want the square of : "))
print(Square(n))
