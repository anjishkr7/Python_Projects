# CRUD operation project :-
from pathlib import Path
def readFileAndFolder():
    path=Path('')
    items=list(path.rglob('*'))
    for i, items in enumerate(items):
        print(f"{i+1} : {items}")

def createFile():
  try:
    readFileAndFolder()
    name=input("please tell your file name:- ")
    p=Path(name)
    if not p.exists():
      with open(p,"w") as fs:
        data=input("What u want to write in this file: ")
        fs.write(data)

      print("File created successfully")
    else:
      print("This file already exists")
  except Exception as err:
    print(f"An error occured as {err}")
def readFile():
  try:
    readFileAndFolder()
    name=input("Which file you want to Read: ")
    p=Path(name)
    if p.exists():
      with open(p,'r') as fs:
        data=fs.read()
        print(data)
    else:
      print("File doesn't exists")
  except Exception as err:
    print(f"An error occured as {err}")

print("Press 1 for creating a file")
print("Press 2 for reading a file")
print("Press 3 for updating a file")
print("Press 4 for deleting a file")

check=int(input("please tell your response : "))
if check==1:
    createFile()

if check==2:
  readFile()
