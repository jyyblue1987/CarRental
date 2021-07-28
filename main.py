class Car:
    def __init__(self, number, brand, type, capacity):
        self.number = number
        self.brand = brand
        self.type = type
        self.capacity = capacity

    def set_number(self, number):
        self.number = number

    def get_number(self):
        return self.number

    def set_brand(self, brand):
        self.brand = brand

    def get_brand(self):
        return self.brand

    def set_type(self, type):
        self.type = type

    def get_type(self):
        return self.type

    def set_capacity(self, capacity):
        self.type = capacity

    def get_capacity(self):
        return self.capacity

    def __str__(self):
        return f"Number: {self.number}, Brand: {self.brand}, Type: {self.type}, Capacity: {self.capacity}"

    
        
class CarRental:
    def __init__(self):
        self.cars = []

    def get_cars(self):
        return self.cars

    def add_car(self, car):
        self.cars.append(car)

    def get_cars_by_capacity(self, capacity):
        return [c for c in self.cars if c.get_capacity() == capacity]

    def display_all(self):        
        headers = ["Number", "Brand", "Type", "Capacity"]
        row_format = "{:>15}" * (len(headers) + 1)
        print(row_format.format("No", *headers))

        index = 0
        for c in self.cars:
            print(row_format.format(str(index + 1), *[c.get_number(), c.get_brand(), c.get_type(), c.get_capacity()]))
            index += 1 
            

# Write the driver to test your class.    
def main():
    car_rental = CarRental()

    car1 = Car('111', 'Benz', 'Sedan', 4)
    car2 = Car('222', 'Audi', 'SUV', 6)
    car3 = Car('333', 'BMW', 'Truck', 7)

    car_rental.add_car(car1)
    car_rental.add_car(car2)
    car_rental.add_car(car3)

    cars_by_capacity_6 = car_rental.get_cars_by_capacity(6)
    for c in cars_by_capacity_6:
        print(c)

    car_rental.display_all()

    
    

if __name__ == "__main__":
    main()