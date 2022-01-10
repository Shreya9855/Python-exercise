#Write a function to compute 5/0 and use try/except to catch the exceptions.

def example():
    try:
        div = 5/0
    except ZeroDivisionError as e:
        print("You cannot divide any number by zero")
    
example()

