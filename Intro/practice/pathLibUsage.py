from pathlib import Path

current = Path('.')
print('The current directory is: ', current.resolve(),'\n \n')

# to see everything in the current dir

print("\n ---- content of the current directory -----")
for item in current.iterdir():
    print(item.name, '| is file: ', item.is_file(), '| is directory: ', item.is_dir() )
    
    
# create a folder

new_folder = Path('andy')
try:
    new_folder.mkdir()
    print(f"folder {new_folder} created")
except FileExistsError:
    print(f"folder {new_folder} already exists")