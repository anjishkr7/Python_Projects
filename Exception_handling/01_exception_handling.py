age=int(input("Enter your age: "))
try:
  if age<10 or age>18:
    raise ValueError("your age must be between 10 and 18")
  else:
    print("Welcome to the school")
except Exception as err:
  print(f"An Error occured as {err}")
