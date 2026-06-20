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
    if not p.exists() and p.is_file():
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
    if p.exists() and p.is_file():
      with open(p,'r') as fs:
        data=fs.read()
        print(data)
      print("file Readed succesfully")
    else:
      print("File doesn't exists")
  except Exception as err:
    print(f"An error occured as {err}")
def updateFile():
  try:
    readFileAndFolder()
    name=input("Tell which file you want to update: ")
    p=Path(name)
    if p.exists() and p.is_file():
      print("Press 1 for changing the name of your file: ")
      print("Press 2 for overwriting the data of your file: ")
      print("Press 3 for appending some content in your file: ")
      res=int(input("Tell me your response:- "))
      if res==1:
        name2=input("Tell your new file name: ")
        p2=Path(name2)
        p.rename(p2)
      elif res==2:
        with open(p,'w') as fs:
          data=input("Tell what u want to write this will overwrite the data: ")
          fs.write(data)
      elif res==3:
        with open(p,'a') as fs:
          data=input("Tell me what u want to append : ")
          fs.write(" "+data)
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

if check==3:
  updateFile()
