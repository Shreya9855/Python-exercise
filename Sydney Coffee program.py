import msvcrt
aborted = False
def rateper(quantity):
    if 1 <= quantity <= 5 :
        rate = 36
    elif 6 <= quantity <= 15:
        rate = 34.5
    elif quantity > 15 :
        rate = 32.7
    return rate

def discountRate(reseller):
    if reseller.upper() == "YES":
        discount = 0.2
    else:
        discount = 0
    return discount

while True: 
    name = input("Enter the customer name: " )
    quantity = int(input("Enter the number of coffee bags(1kg) : "))
    rate = rateper(quantity)
    price = quantity * rate
    reseller =input ("Enter yes/no for reseller: ")
    discountPrice = discountRate(reseller) * price
    totalSales = price - discountPrice
    print("Total Sales : " + str(totalSales) )
    print("*****************************************************************************")
    if msvcrt.kbhit() and msvcrt.getch() == chr(27).encode():
        break
print("Thank you ")