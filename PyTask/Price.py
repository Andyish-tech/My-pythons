# Task 2

class Product:
    def __init__(prd, name, price, quantity):
        prd.name=name
        prd.price=price
        prd.quantity=quantity
    
    def Pprice(prd):
        prd.quantity==5
        value= prd.price * prd.quantity
        print(f"The product:{prd.name}, and price per one: {prd.price} the total from stock: {value}")
    def sales(prd, order):
        order=int(input("Enter the quantity you want"))
        if (order<=prd.quantity):
            orderP=prd.price * order
            print(f"Bill: {orderP}")
        else:
            print("You don't have enough stock for this sell")


# Correct answer was

product="Rice"
price=1200
qty=5

Total= price * 5
print(f"The product:{product}, and price per one: {price} the total from stock: {qty}")

bought=int(input("Enter quantity you need"))

if (bought<=qty):
    bill= price * bought
    print(f"Amount: {bill}")
else:
    print("We Dont have enough in stock")



# Task 2 


