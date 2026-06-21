class Animal:
  def __init__(self,name):
    self.name=name
  def show(self):
    print(f"hello i am {self.name}")
class Human(Animal):
  def __init__(self, name,age):
    super().__init__(name)
    self.age=age
  def show(self):
    print(f"hello i am {self.name} and i am {self.age} years old")

person1=Human("Anjish",21)
animal1=Animal("Lion")
animal1.show()
person1.show()

