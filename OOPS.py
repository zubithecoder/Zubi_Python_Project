class Car:
  def __init__(self,name,model,year,color,engine):
      self.name = name
      self.model = model
      self.year = year
      self.color = color
      self.engine = engine

  def display(self):
      print(f" Your car details are: {self.name} {self.model} {self.year} {self.color}")
  def start_engine(self):
      if self.engine >= 0:
          print("Your engine is start")
      else:
          self.engine = 1
          print("Your engine is start now")

  def stop_engine(self):
      if self.engine == 0:
          print("Your engine is stopped now")


# Test the Car class
if __name__ == "__main__":
    # Create a car instance
    my_car = Car("Toyota", "Camry", 2023, "Blue", 1)
    
    # Display car details
    my_car.display()
    
    # Test engine methods
    my_car.start_engine()
    my_car.stop_engine() 


# --------------------------------------------


