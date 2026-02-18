import os
# print the current directory
print(os.getcwd())

#check what inside the directory
print(os.listdir('.'))

#Check existance

print(os.path.exists('os.py'))

#Check Information on the file or folder
             # check if is file
print(os.path.isfile('os.py'))
             # check if is folder
print(os.path.isdir('os.py'))