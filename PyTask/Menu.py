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

while True:
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