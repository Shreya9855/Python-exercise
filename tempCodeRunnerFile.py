
        discount = 0.2 * quantity * rate
        return float(discount)
    else:
        return 0

#customer
name = input("Enter your name: ")
quantity = int(input("Enter the number of coffee bags: "))
reseller = input("Are you a reseller? (y/n) :")
Sales = rate(quantity) * quantity - discount(reseller)
print(rate(qua