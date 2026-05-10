# class
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_info(self):
        return f"{self.year} {self.make} {self.model}"

#subclass
class Car(Vehicle):
    def __init__(self, make, model, year, num_doors):
        super().__init__(make, model, year)
        self.num_doors = num_doors

    def get_info(self):
        return f"{super().get_info()} with {self.num_doors} doors"

#subclass
class ElectricCar(Car):
    def __init__(self, make, model, year, num_doors, battery_size):
        super().__init__(make, model, year, num_doors)
        self.battery_size = battery_size

    def get_info(self):
        return f"{super().get_info()} and a {self.battery_size}-kWh battery"

#subclass
class HyperCar(Car):
    def __init__(self, make, model, year, num_doors, top_speed):
        super().__init__(make, model, year, num_doors)
        self.top_speed = top_speed

    def get_info(self):
        return f"{super().get_info()} and a top speed of {self.top_speed} mph"

#output
car1 = Car("Toyota", "Corolla", 2020, 4)
tesla = ElectricCar("Tesla", "Model 3", 2024, 4, 75)
print (Car.get_info(car1))
print(ElectricCar.get_info(tesla))