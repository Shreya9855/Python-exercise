#Write a program which can map() and filter() to make a list whose elements are square of even number in [1,2,3,4,5,6,7,8,9,10].

lst = [0,1,2,3,4,5,6,7,8,9]
even_list = list(filter(lambda n:n%2 ==0 ,lst))
square_even = list(map(lambda n :n *n,even_list))
print(square_even)
