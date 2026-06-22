class Animal:
  def __init__(self,name):
    self.name=name
class Human:
  def __init__(self,name,age):
    self.name=name
    self.age=age
class Robots(Animal,Human):
  def __init__(self, name,age,gender):
    # super().__init__(name)
    Human.__init__(self,name,age)
    self.gender=gender


obj=Robots("Lion",32,"Female")
print(obj.name)
