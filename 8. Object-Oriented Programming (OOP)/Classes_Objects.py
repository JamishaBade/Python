class Car:
    def __init__(self, price, brand, color):
        self.price = price
        self.brand = brand
        self.color = color

    def start(self):
        print(f"{self.brand} does burrr")

    def run(self):
        print(f"{self.brand} starts running")

    def __str__(self):
        return f"{self.brand} ({self.color}) costs ${self.price}"


car_1 = Car(920000, "BMW", "Black")
car_2 = Car(290000, "Mercedes", "Yellow")
car_1.start()
car_2.start()
car_2.run()
print(car_1)
print(car_2)
