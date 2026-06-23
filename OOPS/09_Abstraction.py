from abc import ABC,abstractmethod

class RequiredForAll(ABC):
  @abstractmethod
  def perimeter(self):
    print("Parent perimeter called")

  @abstractmethod
  def area(self):
    print("Parent area called")

class Square(RequiredForAll):
  def __init__(self,side):
    self.side=side
  def perimeter(self):
    super().perimeter()
    print(2*self.side)
  def area(self):
    super().area()
    print(self.side*self.side)


obj=Square(7)

obj.area()
