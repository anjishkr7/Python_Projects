class Factory:
  def __init__(self,material,zips):
    self.material=material
    self.zips=zips
class DelhiFactory(Factory):
  def __init__(self, material, zips,color):
    super().__init__(material, zips)
    self.color=color
class PuneFactory(DelhiFactory):
  def __init__(self, material, zips, color,pockets):
    super().__init__(material, zips, color)
    self.pockets=pockets
obj=PuneFactory("Leather",2,"Red",4)
print(obj.material)
