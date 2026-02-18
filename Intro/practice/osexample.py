import os as ish

# create a folder

try:
    ish.mkdir('example')
    print('Folder is created succesfully')
except FileExistsError:
    print("Folder you want to create alread exists")
    
# print(ish.listdir('.'))

file_path= 'hello.txt'

try:
    with open(file_path, 'w') as file:
        file.write('Hello level 5 pionerr. \n')
        file.write('file handling is not hard as you said')
    print(f"File '{file_path}'create successfully")
except IOError as err:
    print(f"something went wrong while creating file: {err}")
    
print(ish.path.exists(file_path))    