#Name: Cassandra Corbin
#Date:April 8, 2024
#Program: This is a program that takes in the the type of vechicle inputed and assigns it to the superclass, then takes attributes of a car, and assigns them to a lower class. The program will then display the information.



class Vehicle: #Create super class
    def __init__(self):  #Initialize attributes
        self.vehicle_type = None
    def set_vehicle_type(self, vehicle_type):
        self.vehicle_type = vehicle_type
class Automobile(Vehicle):   #Create class
    def __init__(self):
        super().__init__()
        self.year = None
        self.make = None
        self.model = None
        self.doors = None
        self.roof = None
    def set_attributes(self, year, make, model, doors, roof):
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof
    def display_details(self):       #Displays information of the car
        print("Vehicle type: {}".format(self.vehicle_type))
        print("Year: {}".format(self.year))
        print("Make: {}".format(self.make))
        print("Model: {}".format(self.model))
        print("Number of doors: {}".format(self.doors))
        print("Type of roof: {}".format(self.roof))
def main():
    car = Automobile()
    vehicle_type = "car"
    year = input("Enter the year: ") #Prompts the user for the year
    make = input("Enter the make: ") #Prompts the user for the make
    model = input("Enter the model: ")  #Prompts the user for the model
    doors = input("Enter the number of doors: ") #Prompts the user for the number of doors
    roof = input("Enter the type of roof: ")  #Prompt the user for the type of roof
    car.set_vehicle_type(vehicle_type)  #Sets the vehicle type of the car
    car.set_attributes(year, make, model, doors, roof)  #Sets the attributes of the car
    print("\nCar Details:")
    car.display_details()  #Displays the car details
if __name__ == "__main__":
    main()   #End of program