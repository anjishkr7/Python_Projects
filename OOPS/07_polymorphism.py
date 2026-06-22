class Animal:
  def show(self):
    print("hello there!")
class Human(Animal):
  def show(self):      #Metohd Overridding
    print("Good Morning")
obj = Human()
obj.show()





