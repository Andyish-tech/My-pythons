import os

# create a folder

try:
    os.mkdir('example')
    print('Folder is created succesfully')
except FileExistsError:
    print("Folder you want to create alread exists")
    
print(os.listdir('.'))