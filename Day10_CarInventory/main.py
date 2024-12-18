class Car:
  def __init__(self, make, model, year, price):
    self.make = make
    self.model = model
    self.year = year
    self._price = price
    
  def __repr__(self):
    return f"Make: {self.make}, Model: {self.model}, Year: {self.year}, Price: {self.price}"
  
    
  # This function return the price and this function can be called as property   
  @property
  def price(self):
    return self._price
  
  # Set new price to price only if price is greater then 0 
  @price.setter
  def price(self, new_price):
    if new_price <= 0:
      raise ValueError("Price cannot be zero or negative.")
      
    self._price = new_price
    
  
    
class Dealership(Car):
  inventory = {}


  # This function adds car in the inventory
  @classmethod
  def add_cars(cls, car):
    # Check if car with the same make and year already exists
    if (car.make, car.year) in cls.inventory:
      print(f"Car '{car.make}' from year {car.year} already exists in the inventory.")
      return
    
    # Add the car using (make, year) as the key
    cls.inventory[(car.make, car.year)] = car

    
   
  @classmethod
  def display_inventory(cls):
    for car in cls.inventory.values():
      print(car)
    
      
    
    
car1 = Car("Toyota", "Camry",2024,  20000)
car2 = Car("Ford", "Mustang", 2021, 35000)
car3 = Car("Ford", "Mustang", 2024, 35000)
car4 = Car("Ford", "Mustang", 2024, 35000)



Dealership.add_cars(car1)
Dealership.add_cars(car2)
Dealership.add_cars(car3)
Dealership.add_cars(car4)



Dealership.display_inventory()

print(car1.price)

# car1.price = 0

# print(car1.price)