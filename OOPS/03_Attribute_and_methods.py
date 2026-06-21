class Animal:
  name="Lion" #class Attribute

  def __init__(self,age):
    self.age=age #instance Attribute

  def show(self): #instance method
    print(f"How are you, your are is {self.age}")
  @classmethod
  def hello(cls):#classmethod
    print("How are you bro!")
  @staticmethod
  def static():
    print("How are u")

obj =Animal(12)
obj.show()
obj.hello()
obj.static()
