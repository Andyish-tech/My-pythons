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
    
print("exists?: ", new_folder.exists())
print("is directory?: ", new_folder.is_dir())
print("is file?: ", new_folder.is_file(),"\n")

# Nested folders

nested = Path('david/wivine/gisubizo')
nested.mkdir(parents= True, exist_ok=True)
print("nested folder ", {nested})

file_path = Path('david/wivine.txt')
file_path.write_text("I love you David \n  'wivine'")
print(f"file{file_path} created successfully")

cartoon = file_path.read_text()
print(" \n ----- cartoon content -----")
print(cartoon)