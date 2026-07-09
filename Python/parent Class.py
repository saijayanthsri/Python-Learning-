#parent Class
class vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def show_details(self):
        print("Brand:", self.brand)
        print("Model:", self.model)


#class(car)
class Car(vehicle):
    def __init__(self, brand, model, seat_capacity):
        super().__init__(brand, model)
        self.seat_capacity = seat_capacity

    def rental_price(self, days):
        return days * 1000

    def show_details(self):
        super().show_details()
        print("Seat Capacity:", self.seat_capacity)

#class(bike)
class Bike(vehicle):
    def __init__(self, brand, model, seat_capacity):
        super().__init__(brand, model)
        self.seat_capacity = seat_capacity

    def rental_price(self, days):
        return days * 500

    def show_details(self):
        super().show_details()
        print("Bike capacity:", self.seat_capacity)
        


car = Car("Maruti","Alto", "5")
bike = Bike("Jawa","Thunderbird", "350cc")

days = int(input("Enter number of rental days: "))
cars = input("Enter car brand from the list (Maruti, Volkswagen, Tata, Hyundai, Mahindra): ")
bikes = input("Enter bike brand from the list (Jawa, Royal Enfield, Bajaj, KTM, Hero): ")

print("\nCar Details")
car.show_details()
print("Rental Price:", car.rental_price(days))

print("\nBike details")
bike.show_details()
print("Rental price:", bike.rental_price(days))
