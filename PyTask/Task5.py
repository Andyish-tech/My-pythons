import json
import os

FILE_NAME = "products.txt"

def load_products():
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r", encoding="utf-8") as file:
                return json.load(file)
        except json.JSONDecodeError:
            print("Warning: File is empty or corrupted. Starting fresh.")
            return []
    return []

def save_products(products):
    try:
        with open(FILE_NAME, "w", encoding="utf-8") as file:
            json.dump(products, file, indent=4)
    except IOError as e:
        print(f"Error saving file: {e}")

def add_product(pName, Price):
    if not isinstance(pName, str) or not pName.strip():
        print("Invalid product name.")
        return
    if not isinstance(Price, (int, float)) or Price < 0:
        print("Invalid price.")
        return

    newP = {"name": pName.strip(), "price": Price}
    Products.append(newP)
    save_products(Products)
    print(f"Product '{pName}' added successfully.")

def clear_file():
    if os.path.exists(FILE_NAME):
       os.remove(FILE_NAME)
    open(FILE_NAME, 'w').close()
    print("File reset successfully.")

Products = load_products()

clear_file()
print(f"Current Products: ", Products)
