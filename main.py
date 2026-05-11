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

#class: printing info
class CarInfoPrinter:
    @staticmethod #clear screen
    def clear_screen():
        print("\033[H\033[J", end="")

    @staticmethod #printing info
    def print_cars_info(cars):
        for car in cars:
            print(f"{car.year} {car.make} {car.model} with {car.num_doors} doors")

    @staticmethod #menu
    def display_menu():
        CarInfoPrinter.clear_screen() #clearing the screen first
        while True:
            print("\nMenu:")
            print("1. Print all cars")
            print("2. Exit")
            choice = input("Enter your choice: ")
            if choice == "1":
                CarInfoPrinter.print_cars_info(cars)
            elif choice == "2":
                print ("Exiting the program.")
                break
            else:
                print("Invalid choice. Please try again.")

#data
cars = [
    Car("Chevrolet", "Convertible", 1938, 2),
    Car("Volkswagen", "Beetle", 1967, 2),
    Car("Porsche", "356B", 1960, 2),
    Car("Alfa Romeo", "2600 Sprint", 1965, 2),
    Car("Ford", "Mustang", 1966, 2),
    Car("Mercedes-Benz", "220SE", 1964, 4),
    Car("Ferrari", "365 GT 2+2", 1967, 2),
    Car("Ford", "Falcon", 1962, 4)
]

#display the menu
CarInfoPrinter.display_menu()