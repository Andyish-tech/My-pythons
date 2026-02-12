# Task 2

p1="Check price"
p2="Calculate total"
p3="Exit"
price= 1200
def menu():
    print("our menu")
    print(f"1. {p1}")
    print(f"2. {p2}")
    print(f"3. {p3}")

def riceP():
    print(f"The price of rice is {price}")
def total():
    qty=int(input("Enter quantity"))
    Total= qty *price
    print(f"The Total price is: {Total}")

while False:
    menu()
    option=input("Choose between 1-3: ")
    
    if option=='1':
        riceP()   
    elif option=='2':
        total()
    elif option=='3':
        print("Goodbye")
        exit()
    else:
        print("Invalid option")
 
#Task 4
 
Products=[{
    "name":"sugar",
    "price":1500
},{
    "name":"Soap",
    "price": 800
},{
    "name":"Rice",
    "price":"1200"
}

]
    
def add_product(pName, Price):
    # pName=input("Insert Product name: ")
    # Price=int(input("Add its price"))
    newP={"name":pName,"price":Price}
    Products.append(newP)
    return Products
def show_product():
    for index, product in enumerate(Products, start=1):
     print(f"{index}. {product['name']} Cost: {product['price']}")
add_product("Cassava", 1200)
show_product()
add_product("Potato", 1500)
