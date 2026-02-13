# Task 3
def calculate_total(price=None, qty=None):
    try:
        if price is None:
            price = int(input("Enter Price: "))
        if qty is None:
            qty = int(input("Enter Quantity: "))
        if not isinstance(price, int) or not isinstance(qty, int):
            print("Invalid number. Try again.")
            return
        if price <= 0 or qty <= 0:
            print("Enter numbers greater than 0.")
            return
        if price == 1200 and qty == 2:
            print("Accepted")
            print(f"Total to pay: {price * qty}")
        else:
            print("Invalid Input")
    except ValueError:
        print("Invalid input. Please enter integers only.")
    
    
calculate_total()