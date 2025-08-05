from abc import ABC, abstractmethod

# 1. Abstraction - Define abstract base class

class vehicle(ABC):
  def __init__(self, brand, model):
    self.brand = brand               # Public
    self._model = model              # Protected
    self.__engine_status = False     # Private

  def start_engine (self):
    self.__engine_status = True
    print(f"{self.brand} {self._model} engin started. ")

  def stop_engine (self):
    self.__engine_status = False
    print(f"{self.brand} {self._model} engin stoped. ")

  def get_engine_status(self):
    return self.__engine_status



  # Abstract method
  @abstractmethod
  def display_info(self):
    pass


# 2. Inheritance - Car inherits from Vehicle

class Car(vehicle):
  def __init__(self, brand, model, seats):
    super().__init__(brand, model)           # Call parent constructor
    self.seats = seats 

  def display_info(self):                     # Polymorphism (overriding)
    print(f"Car: {self.brand} {self._model}, Status: {self.seats}")


# 3. Inheritance - Bike inherits from Vehicle
class Bike(vehicle):
  def __init__(self, brand, model,  type_of_bike):
    super().__init__(brand, model)
    self.type_of_bike = type_of_bike


  def display_info(self):        # Polymorphism (overriding)
    print(f"Bike: {self.brand} {self._model}, Type: {self.type_of_bike}")




# 4. Object creation and using encapsulated methods
car1 = Car("Toyota",  "Fortuner", 7)
bike1 = Bike("Yamaha", "R15", "Sports")

# Use methods

car1.start_engine()
car1.display_info()
print("Engine Status: ", car1.get_engine_status())
car1.stop_engine()
print("--------------------------------")

bike1.start_engine()
bike1.display_info()
print("Engine Status: ", bike1.get_engine_status())
bike1.start_engine()


