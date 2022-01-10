#Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.

n = input("Enter a number")
sum = "a+aa+aaa+aaaa"
numSum = (sum.replace("a", n))
a = eval(numSum)
print(a)