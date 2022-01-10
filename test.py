# rate and price
def rateper(quantity):
    if 1 <= quantity <= 5 :
        rate = 36
    elif 6 <= quantity <= 15:
        rate = 34.5
    elif quantity > 15 :
        rate = 32.7
    return rate

#user
name = input("Enter the customer name: " )
quantity = int(input("Enter the number of coffee bags(1kg) : "))
rate = rateper(quantity)
print("rate: " + str(rate))
price = quantity * rate
print("price : " + str(price))
reseller =input ("Enter yes/no for reseller: ")

def discountRate(reseller):
    if reseller.upper() == "YES":
        discount = 0.2
    else:
        discount = 0
    return discount

print("discount rate "+ str(discountRate(reseller)))
discountPrice = discountRate(reseller) * price
print("discount price: "+ str(discountPrice))

totalSales = price - discountPrice
print(totalSales)
